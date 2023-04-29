import os

from matplotlib import backend_bases, projections
from matplotlib.artist import Artist, allow_rasterization
from matplotlib.axes import Axes, SubplotBase
from matplotlib.backend_bases import (
    DrawEvent,
    FigureCanvasBase,
    MouseButton,
    MouseEvent,
    NonGuiException,
    RendererBase,
)
from matplotlib.colors import Colormap, Normalize
from matplotlib.colorbar import Colorbar
from matplotlib.cm import ScalarMappable
from matplotlib.gridspec import GridSpec, SubplotSpec
from matplotlib.image import _ImageBase, FigureImage
from matplotlib.layout_engine import (
    ConstrainedLayoutEngine,
    LayoutEngine,
    PlaceHolderLayoutEngine,
    TightLayoutEngine,
)
from matplotlib.legend import Legend
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle, Patch
from matplotlib.text import Text
from matplotlib.transforms import (
    Affine2D,
    Bbox,
    BboxBase,
    BboxTransformTo,
    TransformedBbox,
    Transform,
)

import numpy as np
from numpy.typing import ArrayLike

from collections.abc import Callable, Iterable
from typing import Any, IO, Literal, overload
from .typing import ColorType, HashableList

class SubplotParams:
    def __init__(
        self,
        left: float | None = ...,
        bottom: float | None = ...,
        right: float | None = ...,
        top: float | None = ...,
        wspace: float | None = ...,
        hspace: float | None = ...,
    ) -> None: ...
    left: float
    right: float
    bottom: float
    top: float
    wspace: float
    hspace: float
    def update(
        self,
        left: float | None = ...,
        bottom: float | None = ...,
        right: float | None = ...,
        top: float | None = ...,
        wspace: float | None = ...,
        hspace: float | None = ...,
    ) -> None: ...

class FigureBase(Artist):
    artists: list[Artist]
    lines: list[Line2D]
    patches: list[Patch]
    texts: list[Text]
    images: list[_ImageBase]
    legends: list[Legend]
    subfigs: list[SubFigure]
    stale: bool
    suppressComposite: bool | None
    def __init__(self, **kwargs) -> None: ...
    def autofmt_xdate(
        self,
        bottom: float = ...,
        rotation: int = ...,
        ha: Literal["left", "center", "right"] = ...,
        which: Literal["major", "minor", "both"] = ...,
    ) -> None: ...
    def get_children(self) -> list[Artist]: ...
    def contains(self, mouseevent: MouseEvent) -> tuple[bool, dict[Any, Any]]: ...
    def suptitle(self, t: str, **kwargs) -> Text: ...
    def get_suptitle(self) -> str: ...
    def supxlabel(self, t: str, **kwargs) -> Text: ...
    def get_supxlabel(self) -> str: ...
    def supylabel(self, t: str, **kwargs) -> Text: ...
    def get_supylabel(self) -> str: ...
    def get_edgecolor(self) -> ColorType: ...
    def get_facecolor(self) -> ColorType: ...
    def get_frameon(self) -> bool: ...
    def set_linewidth(self, linewidth: float) -> None: ...
    def get_linewidth(self) -> float: ...
    def set_edgecolor(self, color: ColorType) -> None: ...
    def set_facecolor(self, color: ColorType) -> None: ...
    def set_frameon(self, b: bool) -> None: ...
    @property
    def frameon(self) -> bool: ...
    @frameon.setter
    def frameon(self, b: bool) -> None: ...
    def add_artist(self, artist: Artist, clip: bool = ...) -> Artist: ...
    @overload
    def add_axes(self, ax: Axes) -> Axes: ...
    @overload
    def add_axes(
        self,
        rect: tuple[float, float, float, float],
        projection: None | str = ...,
        polar: bool = ...,
        **kwargs
    ) -> Axes: ...

    # TODO: docstring indicates SubplotSpec a valid arg, but none of the listed signatures appear to be that
    @overload
    def add_subplot(
        self, nrows: int, ncols: int, index: int | tuple[int, int], **kwargs
    ) -> Axes: ...
    @overload
    def add_subplot(self, pos: int, **kwargs) -> Axes: ...
    @overload
    def add_subplot(self, ax: Axes, **kwargs) -> Axes: ...
    @overload
    def add_subplot(self, ax: SubplotSpec, **kwargs) -> Axes: ...
    @overload
    def add_subplot(self, **kwargs) -> Axes: ...
    @overload
    def subplots(
        self,
        nrows: int = ...,
        ncols: int = ...,
        *,
        sharex: bool | Literal["none", "all", "row", "col"] = ...,
        sharey: bool | Literal["none", "all", "row", "col"] = ...,
        squeeze: Literal[False],
        width_ratios: ArrayLike | None = ...,
        height_ratios: ArrayLike | None = ...,
        subplot_kw: dict[str, Any] | None = ...,
        gridspec_kw: dict[str, Any] | None = ...
    ) -> np.ndarray: ...
    @overload
    def subplots(
        self,
        nrows: int = ...,
        ncols: int = ...,
        *,
        sharex: bool | Literal["none", "all", "row", "col"] = ...,
        sharey: bool | Literal["none", "all", "row", "col"] = ...,
        squeeze: bool = ...,
        width_ratios: ArrayLike | None = ...,
        height_ratios: ArrayLike | None = ...,
        subplot_kw: dict[str, Any] | None = ...,
        gridspec_kw: dict[str, Any] | None = ...
    ) -> np.ndarray | SubplotBase | Axes: ...
    def delaxes(self, ax: Axes) -> None: ...
    def clear(self, keep_observers: bool = ...) -> None: ...
    def clf(self, keep_observers: bool = ...) -> None: ...

    @overload
    def legend(self) -> Legend: ...
    @overload
    def legend(self, handles: Iterable[Artist], labels: Iterable[str], **kwargs) -> Legend: ...
    @overload
    def legend(self, *, handles: Iterable[Artist], **kwargs) -> Legend: ...
    @overload
    def legend(self, labels: Iterable[str], **kwargs) -> Legend: ...
    @overload
    def legend(self, **kwargs) -> Legend: ...

    def text(
        self,
        x: float,
        y: float,
        s: str,
        fontdict: dict[str, Any] | None = ...,
        **kwargs
    ) -> Text: ...
    def colorbar(
        self,
        mappable: ScalarMappable,
        cax: Axes | None = ...,
        ax: Axes | Iterable[Axes] | None = ...,
        use_gridspec: bool = ...,
        **kwargs
    ) -> Colorbar: ...
    def subplots_adjust(
        self,
        left: float | None = ...,
        bottom: float | None = ...,
        right: float | None = ...,
        top: float | None = ...,
        wspace: float | None = ...,
        hspace: float | None = ...,
    ) -> None: ...
    def align_xlabels(self, axs: Iterable[Axes] | None = ...) -> None: ...
    def align_ylabels(self, axs: Iterable[Axes] | None = ...) -> None: ...
    def align_labels(self, axs: Iterable[Axes] | None = ...) -> None: ...
    def add_gridspec(self, nrows: int = ..., ncols: int = ..., **kwargs) -> GridSpec: ...
    @overload
    def subfigures(
        self,
        nrows: int = ...,
        ncols: int = ...,
        squeeze: Literal[False] = ...,
        wspace: float | None = ...,
        hspace: float | None = ...,
        width_ratios: ArrayLike | None = ...,
        height_ratios: ArrayLike | None = ...,
        **kwargs
    ) -> np.ndarray: ...
    @overload
    def subfigures(
        self,
        nrows: int = ...,
        ncols: int = ...,
        squeeze: Literal[True] = ...,
        wspace: float | None = ...,
        hspace: float | None = ...,
        width_ratios: ArrayLike | None = ...,
        height_ratios: ArrayLike | None = ...,
        **kwargs
    ) -> np.ndarray | SubFigure: ...
    def add_subfigure(self, subplotspec: SubplotSpec, **kwargs) -> SubFigure: ...
    def sca(self, a: Axes) -> Axes: ...
    def gca(self) -> Axes: ...
    def _gci(self) -> ScalarMappable | None: ...
    def _process_projection_requirements(
        self, *args, axes_class=None, polar=False, projection=None, **kwargs
    ) -> tuple[type[Axes], dict[str, Any]]: ...
    def get_default_bbox_extra_artists(self) -> list[Artist]: ...
    def get_tightbbox(
        self,
        renderer: RendererBase | None = ...,
        bbox_extra_artists: Iterable[Artist] | None = ...,
    ) -> Bbox: ...

    # Any in list of list is recursive list[list[Hashable | list[Hashable | ...]]] but that can't really be type checked
    def subplot_mosaic(
        self,
        mosaic: str | HashableList,
        *,
        sharex: bool = ...,
        sharey: bool = ...,
        width_ratios: ArrayLike | None = ...,
        height_ratios: ArrayLike | None = ...,
        empty_sentinel: Any = ...,
        subplot_kw: dict[str, Any] | None = ...,
        per_subplot_kw: dict[Any, dict[str, Any]] | None = ...,
        gridspec_kw: dict[str, Any] | None = ...
    ) -> dict[Any, Axes]: ...

class SubFigure(FigureBase):
    figure: Figure
    subplotpars: SubplotParams
    dpi_scale_trans: Affine2D
    canvas: FigureCanvasBase
    transFigure: Transform
    bbox_relative: Bbox
    figbbox: Bbox
    bbox: Bbox
    transSubfigure: Transform
    patch: Rectangle
    def __init__(
        self,
        parent: Figure | SubFigure,
        subplotspec: SubplotSpec,
        *,
        facecolor: ColorType | None = ...,
        edgecolor: ColorType | None = ...,
        linewidth: float = ...,
        frameon: bool | None = ...,
        **kwargs
    ) -> None: ...
    @property
    def dpi(self) -> float: ...
    @dpi.setter
    def dpi(self, value: float) -> None: ...
    def get_dpi(self) -> float: ...
    def set_dpi(self, val) -> None: ...
    def get_constrained_layout(self) -> bool: ...
    def get_constrained_layout_pads(
        self, relative: bool = ...
    ) -> tuple[float, float, float, float]: ...
    def get_layout_engine(self) -> LayoutEngine: ...
    @property  # type: ignore[misc]
    def axes(self) -> list[Axes]: ...  # type: ignore[override]
    def get_axes(self) -> list[Axes]: ...

class Figure(FigureBase):
    figure: Figure
    bbox_inches: Bbox
    dpi_scale_trans: Affine2D
    bbox: Bbox
    figbbox: Bbox
    transFigure: Transform
    transSubfigure: Transform
    patch: Rectangle
    subplotpars: SubplotParams
    def __init__(
        self,
        figsize: tuple[float, float] | None = ...,
        dpi: float | None = ...,
        *,
        facecolor: ColorType | None = ...,
        edgecolor: ColorType | None = ...,
        linewidth: float = ...,
        frameon: bool | None = ...,
        subplotpars: SubplotParams | None = ...,
        tight_layout: bool | dict[str, Any] | None = ...,
        constrained_layout: bool | dict[str, Any] | None = ...,
        layout: Literal["constrained", "compressed", "tight"]
        | LayoutEngine
        | None = ...,
        **kwargs
    ) -> None: ...
    def pick(self, mouseevent: MouseEvent) -> None: ...
    def set_layout_engine(
        self,
        layout: Literal["constrained", "compressed", "tight", "none"]
        | LayoutEngine
        | None = ...,
        **kwargs
    ) -> None: ...
    def get_layout_engine(self) -> LayoutEngine | None: ...
    def show(self, warn: bool = ...) -> None: ...
    @property  # type: ignore[misc]
    def axes(self) -> list[Axes]: ...  # type: ignore[override]
    def get_axes(self) -> list[Axes]: ...
    @property
    def dpi(self) -> float: ...
    @dpi.setter
    def dpi(self, dpi: float) -> None: ...
    def get_tight_layout(self) -> bool: ...
    def get_constrained_layout_pads(
        self, relative: bool = ...
    ) -> tuple[float, float, float, float]: ...
    def get_constrained_layout(self) -> bool: ...
    canvas: FigureCanvasBase
    def set_canvas(self, canvas: FigureCanvasBase) -> None: ...
    def figimage(
        self,
        X: ArrayLike,
        xo: int = ...,
        yo: int = ...,
        alpha: float | None = ...,
        norm: str | Normalize | None = ...,
        cmap: str | Colormap | None = ...,
        vmin: float | None = ...,
        vmax: float | None = ...,
        origin: Literal["upper", "lower"] | None = ...,
        resize: bool = ...,
        **kwargs
    ) -> FigureImage: ...
    def set_size_inches(
        self, w: float | tuple[float, float], h: float | None = ..., forward: bool = ...
    ) -> None: ...
    def get_size_inches(self) -> np.ndarray: ...
    def get_figwidth(self) -> float: ...
    def get_figheight(self) -> float: ...
    def get_dpi(self) -> float: ...
    def set_dpi(self, val: float) -> None: ...
    def set_figwidth(self, val: float, forward: bool = ...) -> None: ...
    def set_figheight(self, val: float, forward: bool = ...) -> None: ...
    def clear(self, keep_observers: bool = ...) -> None: ...
    def draw_without_rendering(self) -> None: ...
    def draw_artist(self, a: Artist) -> None: ...
    def add_axobserver(self, func: Callable[[Figure], Any]) -> None: ...
    def savefig(
        self,
        fname: str | os.PathLike | IO,
        *,
        transparent: bool | None = ...,
        **kwargs
    ) -> None: ...
    def ginput(
        self,
        n: int = ...,
        timeout: float = ...,
        show_clicks: bool = ...,
        mouse_add: MouseButton = ...,
        mouse_pop: MouseButton = ...,
        mouse_stop: MouseButton = ...,
    ) -> list[tuple[int, int]]: ...
    def waitforbuttonpress(self, timeout: float = ...) -> None | bool: ...
    def tight_layout(
        self,
        *,
        pad: float = ...,
        h_pad: float | None = ...,
        w_pad: float | None = ...,
        rect: tuple[float, float, float, float] | None = ...
    ) -> None: ...

def figaspect(arg: float | ArrayLike) -> tuple[float, float]: ...