import statistics
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages
matplotlib.rcParams['text.usetex'] = True

from designinit import beat_with_max_workload

def mean_variance_calculation(prefix, call_fname, n_beat_range):

    beat_vars  = []
    beat_means = [] 
    for n_beat in n_beat_range:
        fname = "result/grid-%s%s-nbeat-%d.npy" % (prefix, call_fname, n_beat)
        grid_table = np.load(fname) 
        _, beats_set, beats_workload = beat_with_max_workload(grid_table)
        beats_workload = np.array(beats_workload) / 3600
        var  = statistics.variance(beats_workload)
        mean = statistics.mean(beats_workload)
        beat_vars.append(var)
        beat_means.append(mean)
    print(beat_means)
    print(beat_vars)
    return np.array(beat_means), np.array(beat_vars)

if __name__ == "__main__":
    # call_fname   = "Jan-APR-2019-PD"
    # n_beat_range = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

    # init_beat_means, init_beat_vars = mean_variance_calculation("", call_fname, n_beat_range)
    # reds_beat_means, reds_beat_vars = mean_variance_calculation("redesign-", call_fname, n_beat_range)

    # with PdfPages("workload-mean-chart.pdf") as pdf:
    #     fig, ax = plt.subplots()

    #     ax.plot(n_beat_range, reds_beat_means/365)
    #     plt.xlabel('number of beats')
    #     plt.ylabel('average workload (hours/day)')
    #     pdf.savefig(fig)

    # with PdfPages("workload-var-chart.pdf") as pdf:
    #     fig, ax = plt.subplots()

    #     l1 = ax.plot(n_beat_range, init_beat_vars)
    #     l2 = ax.plot(n_beat_range, reds_beat_vars)
    #     plt.xlabel('number of beats')
    #     plt.ylabel('variance of beat workload')

    #     ax.legend(('greedy dichotomy', 'heuristic refined'))
    #     pdf.savefig(fig)



    # old_design = np.load("data/grid-Jan-APR-2019-PD.npy")
    # old_x      = old_design[:, 1]
    # _, beats_set, beats_workload0 = beat_with_max_workload(old_design)

    # print(old_design)
    # print(beats_set)
    # print(beats_workload0 / 3600 / 120)

    # new_design1 = np.load("result/grid-Jan-APR-2019-PD-nbeat-15.npy")
    # _, beats_set, beats_workload1 = beat_with_max_workload(new_design1)

    # print(beats_set)
    # print(beats_workload1 / 3600 / 120)

    # new_design2 = np.load("result/grid-redesign-Jan-APR-2019-PD-nbeat-15.npy")
    # _, beats_set, beats_workload2 = beat_with_max_workload(new_design2)

    # print(beats_set)
    # print(beats_workload2 / 3600 / 120)



    new_design2 = np.load("result/grid-redesign-regression-workload-2021-nbeat-18.npy")
    _, beats_set, beats_workload2 = beat_with_max_workload(new_design2)

    print(beats_set)
    print(beats_workload2 / 3600 / 30)

    
    old_design = np.load("data/grid-Jan-APR-2019-PD.npy")
    old_x      = old_design[:, 1]
    old_design = new_design2
    old_design[:, 1] = old_x
    _, beats_set, beats_workload0 = beat_with_max_workload(old_design)

    print(old_design)
    print(beats_set)
    print(beats_workload0 / 3600 / 30)

    new_design1 = np.load("result/grid-Jan-APR-2019-PD-nbeat-18.npy")
    x           = new_design1[:, 1]
    new_design1 = new_design2
    new_design1[:, 1] = x
    _, beats_set, beats_workload1 = beat_with_max_workload(new_design1)

    print(beats_set)
    print(beats_workload1 / 3600 / 30)

    print(np.var(beats_workload0 / 3600 / 30))
    print(np.var(beats_workload1 / 3600 / 30))
    print(np.var(beats_workload2 / 3600 / 30))