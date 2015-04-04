# [PyClean](https://github.com/bzaczynski/pyclean)

[Sublime Text 3](http://www.sublimetext.com) plugin for removal of Python binary artifacts such as `*.pyc` files.

### Installation

```
$ cd ~/.config/sublime-text-3/Packages
$ git clone git@github.com:bzaczynski/pyclean.git
```

### Usage

Default shortcut is `Ctrl`+`F8` but this can be overridden by going to menu "Preferences" | "Key Bindings - User" and adding a binding, e.g.

```
{ "keys": ["ctrl+f8"], "command": "py_clean" }
```

### Patterns

The following patterns are used to identify files and folders for removal.

#### Files

```
*.pyc
*.pyo
```

#### Folders

```
build/
dist/
*.egg-info/
```

### License

This project is licensed under the [MIT License](https://raw.githubusercontent.com/bzaczynski/pyclean/master/LICENSE).
