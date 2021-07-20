
def plotPanel(ax, x, y, predictions, p_value, condition,
               xlabel="abs(Speed)", ylabel="Spike Rate", title=None,
               data_color="gray", regression_line_color="red",
               line_style="solid", legend_loc="upper left",
               legend_label_pattern="p={:.04f}"):
    legend_label = legend_label_pattern.format(p_value)
    ax.scatter(x=x, y=y, color=data_color, linestyle=line_style)
    ax.plot(x, predictions, color=regression_line_color, label=legend_label)
    ax.legend(loc=legend_loc)
    if condition=="Visual":
        ax.set_xlabel(xlabel)
    if condition=="VisVes":
        ax.set_ylabel(ylabel)
    if title is None:
        title = condition
    ax.set_title(title)

