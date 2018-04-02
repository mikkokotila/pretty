import seaborn as sns

from ..style.template import _header, _footer
#from ..utils.utils import _limiter, _scaler


def violin(data,
           x,
           y,
           hue=None,
           split=True,
           palette='default',
           style='astetik',
           dpi=72,
           x_label='',
           y_label='',
           x_scale='linear',
           y_scale='linear',
           x_limit='auto',
           y_limit='auto'):

    # HEADER STARTS >>>
    palette = _header(palette, style, n_colors=2, dpi=dpi)  # NOTE: y exception
    # <<< HEADER ENDS

    p = sns.violinplot(data=data,
                       x=x,
                       y=y,
                       hue=hue,
                       palette=palette,
                       split=split,
                       cut=3)

    #FOOTER STARTS >>>
    _footer(p, x_label, y_label)
    #<<< FOOTER ENDS

    p.spines['bottom'].set_color('black')