#!/usr/bin/env python3
"""
Synthetic component-mapping example.

This script creates a toy regional genetic component with synthetic SNP
weights, assigns mock LD blocks and nearby genes, and produces a simple
component annotation table plus a weight-profile figure.

No real genotype, imaging, phenotype or controlled-access data are used.
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


OUT_DATA = Path("data")
OUT_RESULTS = Path("results")
OUT_FIGURES = OUT_RESULTS / "figures"


def make_synthetic_component(seed: int = 42, n_snps: int = 120) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    positions = np.arange(n_snps) * 2_500 + 1_000_000

    # Three broad synthetic LD blocks.
    ld_block = np.select(
        [
            positions < 1_100_000,
            (positions >= 1_100_000) & (positions < 1_220_000),
            positions >= 1_220_000,
        ],
        ["block_1", "block_2", "block_3"], default="unassigned"
    )

    # Synthetic smooth component profile: broad signal plus noise.
    centre_1 = 1_075_000
    centre_2 = 1_245_000

    signal = (
        1.4 * np.exp(-((positions - centre_1) ** 2) / (2 * 28_000**2))
        - 1.0 * np.exp(-((positions - centre_2) ** 2) / (2 * 35_000**2))
    )
    noise = rng.normal(0, 0.15, size=n_snps)
    weights = signal + noise

    genes = np.select(
        [
            positions < 1_070_000,
            (positions >= 1_070_000) & (positions < 1_160_000),
            (positions >= 1_160_000) & (positions < 1_245_000),
            positions >= 1_245_000,
        ],
        ["GENE_A", "GENE_B", "GENE_C", "GENE_D"], default="GENE_UNASSIGNED"
    )

    annotation = np.select(
        [genes == "GENE_A", genes == "GENE_B", genes == "GENE_C", genes == "GENE_D"],
        ["promoter_proximal","enhancer_like", "intronic", "intergenic" ], default="unannotated"
    )

    return pd.DataFrame(
        {
            "snp_id": [f"rsSYN{i:05d}" for i in range(1, n_snps + 1)],
            "position_bp": positions,
            "ld_block": ld_block,
            "nearby_gene": genes,
            "regulatory_annotation": annotation,
            "component_weight": weights,
            "abs_component_weight": np.abs(weights),
        }
    )


def summarise_component(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby(["nearby_gene", "ld_block", "regulatory_annotation"], as_index=False)
        .agg(
            n_snps=("snp_id", "count"),
            mean_abs_weight=("abs_component_weight", "mean"),
            max_abs_weight=("abs_component_weight", "max"),
            signed_weight_sum=("component_weight", "sum"),
        )
        .sort_values("max_abs_weight", ascending=False)
    )

    max_weight = summary["max_abs_weight"].max()
    summary["relative_evidence_score"] = summary["max_abs_weight"] / max_weight

    summary["evidence_tier"] = pd.cut(
        summary["relative_evidence_score"],
        bins=[-np.inf, 0.33, 0.66, np.inf],
        labels=["low", "moderate", "high"],
    )

    return summary


def plot_component_profile(df: pd.DataFrame, output_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(9, 4.8))

    ax.plot(df["position_bp"], df["component_weight"], linewidth=1.6)
    ax.axhline(0, linestyle="--", linewidth=1)

    ax.set_title("Synthetic regional component weight profile")
    ax.set_xlabel("Synthetic genomic position")
    ax.set_ylabel("Component weight")

    for block_name, block_df in df.groupby("ld_block"):
        xmin = block_df["position_bp"].min()
        xmax = block_df["position_bp"].max()
        ax.axvspan(xmin, xmax, alpha=0.08)
        ax.text(
            (xmin + xmax) / 2,
            ax.get_ylim()[1] * 0.88,
            block_name,
            ha="center",
            va="center",
            fontsize=8,
        )

    fig.tight_layout()
    fig.savefig(output_path, dpi=200)
    plt.close(fig)


def main() -> None:
    OUT_DATA.mkdir(parents=True, exist_ok=True)
    OUT_RESULTS.mkdir(parents=True, exist_ok=True)
    OUT_FIGURES.mkdir(parents=True, exist_ok=True)

    component = make_synthetic_component()
    annotation = summarise_component(component)

    component_path = OUT_DATA / "synthetic_component_weights.csv"
    annotation_path = OUT_RESULTS / "synthetic_component_annotation.csv"
    figure_path = OUT_FIGURES / "synthetic_component_weight_profile.png"

    component.to_csv(component_path, index=False)
    annotation.to_csv(annotation_path, index=False)
    plot_component_profile(component, figure_path)

    print(f"Wrote: {component_path}")
    print(f"Wrote: {annotation_path}")
    print(f"Wrote: {figure_path}")


if __name__ == "__main__":
    main()
