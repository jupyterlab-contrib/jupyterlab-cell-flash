# jupyterlab-cell-flash

![Github Actions Status](https://github.com/jtpio/jupyterlab-cell-flash/workflows/Build/badge.svg)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jtpio/jupyterlab-cell-flash/main?urlpath=/lab/tree/demo.ipynb)
[![npm](https://img.shields.io/npm/v/jupyterlab-cell-flash.svg)](https://www.npmjs.com/package/jupyterlab-cell-flash)

JupyterLab extension to show a flash effect when a cell is executed.



## Requirements

* JupyterLab >= 3.0

## Install

```bash
pip install jupyterlab-cell-flash
```

## Settings

Use the following settings to tweak the color and the duration of the animation (in `Settings > Advanced Settings Editor`):

```json5
{
  // The base color for the flash effect
  "color": "rgba(255, 255, 0, 0.5)",

  // The duration of the flash effect animation (in seconds)
  "duration": 0.5
}
```

![settings](https://user-images.githubusercontent.com/591645/82119497-633ffc80-977f-11ea-912f-b0ec57e5f169.gif)

## Contributing

### Development install

Note: You will need NodeJS to build the extension package.

The `jlpm` command is JupyterLab's pinned version of
[yarn](https://yarnpkg.com/) that is installed with JupyterLab. You may use
`yarn` or `npm` in lieu of `jlpm` below.

```bash
# Clone the repo to your local environment
# Change directory to the jupyterlab-cell-flash directory
# Install package in development mode
pip install -e .
# Link your development version of the extension with JupyterLab
jlpm run install:extension
# Rebuild extension Typescript source after making changes
jlpm run build
```

You can watch the source directory and run JupyterLab at the same time in different terminals to watch for changes in the extension's source and automatically rebuild the extension.

```bash
# Watch the source directory in one terminal, automatically rebuilding when needed
jlpm run watch
# Run JupyterLab in another terminal
jupyter lab
```

With the watch command running, every saved change will immediately be built locally and available in your running JupyterLab. Refresh JupyterLab to load the change in your browser (you may need to wait several seconds for the extension to be rebuilt).

### Uninstall

```bash
pip uninstall jupyterlab-cell-flash
jupyter labextension uninstall jupyterlab-cell-flash
```
