import sys
import pdb
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append("../src")
import stats
import plotting

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_filename", help="Data filename",
                        default="../../data/All_three_exp_conditions_4.csv")
    parser.add_argument("--pValues_filename",
                        help="Figure filename pattern",
                        default="../../results/regression_coef_pValues.csv")
    parser.add_argument("--fig_filename_pattern",
                        help="Figure filename pattern",
                        default="../../figures/regression_spikeRateVsAbsSpeed_{:s}.png")

    args = parser.parse_args()
    data_filename = args.data_filename
    pValues_filename = args.pValues_filename
    fig_filename_pattern = args.fig_filename_pattern

    data = pd.read_csv(data_filename, index_col=0)
    conditions = data['Trial Condition'].unique()
    regions = data['Region'].unique()
    regions = [region for region in regions if region is not np.nan]
    p_values = np.empty((len(regions), len(conditions)), dtype=np.double)

    for region_index, region in enumerate(regions):
        fig, axs = plt.subplots(len(conditions), 1)
        for condition_index, condition in enumerate(conditions):
            print("Processing {:s} {:s}".format(region, condition))
            data_subset = data.loc[(data["Trial Condition"]==condition) &
                                   (data["Region"]==region), :]
            x = abs(data_subset["Speed"])
            y = data_subset["Spike Rate"]

            predictions, p_value = stats.linearRegressionAnalysis(x=x, y=y)
            plotting.plotPanel(ax=axs[condition_index], x=x, y=y, 
                               predictions=predictions, p_value=p_value,
                               condition=condition)
            p_values[region_index, condition_index] = p_value
        fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
        fig_filename = fig_filename_pattern.format(region)
        plt.savefig(fig_filename)
    p_values_df = pd.DataFrame(data=p_values, index=regions,
                               columns=conditions)
    p_values_df.to_csv(path_or_buf=pValues_filename)
    pdb.set_trace()

if __name__=="__main__":
    main(sys.argv)
