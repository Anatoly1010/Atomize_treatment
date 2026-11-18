# Atomize treatment

Data treatment tools for [Atomize](https://github.com/Anatoly1010/Atomize). They are optional: the
core runs without them, and a station that wants them lists `atomize-treatment` as a dependency.

```bash
python3 -m pip install -e "path/to/Atomize[math]"
python3 -m pip install -e path/to/Atomize_treatment
```

| Command | Tool |
| --- | --- |
| `atomize-treatment` | 1D data treatment: baseline, smoothing, FFT, fitting, batch processing |
| `atomize-treatment-2d` | 2D data treatment: FFT along an axis, 2D FFT, slices, projections |
| `atomize-deer` | DEER / PDS analysis: background fit and distance distributions |
| `atomize-seqcalc` | Pulse sequence timing and phase-cycling calculator |
| `atomize-excitation` | Pulse excitation and inversion profiles |
| `atomize-spin-sim` | Density-matrix simulation of pulse sequences |

Each tool also runs as `python -m atomize.treatment.<name>`, which is how a station's main window
starts it.

## How it fits with the core and the stations

The files join the core's `atomize` package (there is no `atomize/__init__.py` here), the same way a
station's files do. With a station installed, the tools use its app name, so their files go to that
station's user config folder:

- `treatment/treatment_buffer.csv` and `treatment/treatment_buffer_2d.npz`: the plot that the main
  window's "Send to Data Treatment" hands to the tools;
- `lastdir/*_lastdir.txt`: the folder each tool last opened.

A station can set the Pulse Sequence default grid in its `atomize/station.py`
(`seqcalc_grid = 2.0`; 3.2 ns without it). The spin-dynamics tool opens the station's
`atomize/control_center/experiments/` presets folder when there is one.

The "Makie figure" button of the 1D tool uses Julia and the files in `atomize/treatment/makie/`
(setup in its README).
