---
title: Installing Dependencies
layout: en

redirect_from:
  - /user/apt/
---

<div id="toc"></div>

## Installing Packages on Standard Infrastructure

To install Ubuntu packages that are not included in the default [standard](/user/reference/precise/), use apt-get in the `before_install` step of your `.travis.yml`:

```yaml
before_install:
  - sudo apt-get -qq update
  - sudo apt-get install -y libxml2-dev
```
{: data-file=".travis.yml"}

> Make sure to run `apt-get update` to update the list of available packages (`-qq` for less output). Do not run `apt-get upgrade` as it downloads up to 500MB of packages and significantly extends your build time.
>
> Use the `-y` parameter with apt-get to assume yes as the answer to each apt-get prompt.

### Installing Packages from a custom APT repository

For some packages, you may find an existing repository, which isn't yet set up on our build environment by default. You can easily add custom repositories and Launchpad PPAs as part of your build.

For example, to install gcc from the ubuntu-toolchain ppa

```yaml
before_install:
  - sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y
  - sudo apt-get update -q
  - sudo apt-get install gcc-4.8 -y
```
{: data-file=".travis.yml"}

For repositories not hosted on Launchpad, you need to add a GnuPG key as well.

If you're installing packages this way, make sure you download the correct version for your environment.

This example adds the APT repository for Varnish 3.0 for Ubuntu 12.04 to the locally available list of APT sources and then installs the `varnish` package.

```yaml
before_script:
  - curl http://repo.varnish-cache.org/debian/GPG-key.txt | sudo apt-key add -
  - echo "deb http://repo.varnish-cache.org/ubuntu/ precise varnish-3.0" | sudo tee -a /etc/apt/sources.list
  - sudo apt-get update -qq
  - sudo apt-get install varnish -y
```
{: data-file=".travis.yml"}

### Installing Packages without an APT Repository

For some projects, there may be a Debian/Ubuntu package available, but no corresponding APT repository. These are still easy to install, but require the extra step of downloading.

If you're installing packages this way, make sure you download the correct version for your environment.

Say your project requires the pngquant tool to compress PNG files, here's how to download and install the .deb file:

```yaml
before_install:
  - wget http://pngquant.org/pngquant_1.7.1-1_i386.deb
  - sudo dpkg -i pngquant_1.7.1-1_i386.deb
```
{: data-file=".travis.yml"}

### Installing Packages with the APT Addon

You can also use the APT addon.

This addon provides declarative shortcuts to basic operations of the `apt-get` commands.

If your requirements goes beyond the normal installation, please use another method described above.

#### Adding APT Sources

To add APT sources, you can use one of the following three types of entries:

1. aliases defined in [source whitelist](https://github.com/travis-ci/apt-source-whitelist)
2. `sourceline` key-value pairs which will be added to `/etc/apt/sources.list`
3. when APT sources require GPG keys, you can specify this with `key_url` pairs in addition to `sourceline`.

The following snippet shows these three types of APT sources

```yaml
addons:
  apt:
    sources:
    - deadsnakes
    - sourceline: 'ppa:ubuntu-toolchain-r/test'
    - sourceline: 'deb https://packagecloud.io/chef/stable/ubuntu/precise main'
      key_url: 'https://packagecloud.io/gpg.key'
```
{: data-file=".travis.yml"}

#### Adding APT Packages

List APT packages under the `addons.apt.packages` key:

```yaml
addons:
  apt:
    packages:
    - cmake
    - time
```
{: data-file=".travis.yml"}

> Note: When using APT sources and packages together, you need to make
> sure they are under the same key space in the YAML file. e.g.

```yaml
addons:
  apt:
    sources:
    - ubuntu-toolchain-r-test
    packages:
    - gcc-4.8
    - g++-4.8
```
{: data-file=".travis.yml"}

> Note: If `apt-get install` fails, the build is marked an error.

### Installing Snap Packages

You can install [snap](http://snapcraft.io/) packages in the sudo enabled infrastructure using the Trusty dist:

```yaml
sudo: required
dist: trusty
```
{: data-file=".travis.yml"}


The Ubuntu snap store offers many packages directly maintained by upstream developers, with newer versions than the ones available in the Trusty archive, or even packages that didn't exist when Trusty was released. For example, you can install and run the latest version of [hugo](http://gohugo.io/):

```yaml
sudo: true
dist: trusty

install:
  - sudo apt-get --yes install snapd
  - sudo snap install hugo

script:
  - /snap/bin/hugo new site test-site
```
{: data-file=".travis.yml"}

## Installing Packages on Container Based Infrastructure

To install packages not included in the default [container-based-infrastructure](/user/reference/overview/#virtualization-environments) you need to use the APT addon, as `sudo apt-get` is not available.

### Adding APT Sources

To add APT sources from the [source whitelist](https://github.com/travis-ci/apt-source-whitelist) before your custom build steps, use the `addons.apt.sources` key:

```yaml
addons:
  apt:
    sources:
    - deadsnakes
    - ubuntu-toolchain-r-test
```
{: data-file=".travis.yml"}

### Adding APT Packages

To install packages from the [package whitelist](https://github.com/travis-ci/apt-package-whitelist)  before your custom build steps, use the `addons.apt.packages` key:

```yaml
addons:
  apt:
    packages:
    - cmake
    - time
```
{: data-file=".travis.yml"}

> Note: When using APT sources and packages together, you need to make
> sure they are under the same key space in the YAML file. e.g.

```yaml
addons:
  apt:
    sources:
    - ubuntu-toolchain-r-test
    packages:
    - gcc-4.8
    - g++-4.8
```
{: data-file=".travis.yml"}

> Note: If `apt-get install` fails, the build is marked an error.

#### Identifying the source for a missing package

If you add a package to the APT addon key in your `.travis.yml` but the package is not found, you see a message in the Travis CI build log like this:

```
Installing APT Packages
⋮
E: Unable to locate package libcxsparse3.1.2
E: Couldn't find any package by regex 'libcxsparse3.1.2'
```

To install the package, identify APT source and specify it in the addon key of your `.travis.yml`:

1. Search for the pull request that added the package on GitHub. For example,
   [searching for "libcxsparse3.1.2" ](https://github.com/travis-ci/apt-package-whitelist/search?q=libcxsparse3.1.2&type=Issues&utf8=%E2%9C%93)
   results in [pull request 1194](https://github.com/travis-ci/apt-package-whitelist/pull/1194).

2. Open the pull request, and click the link to the test in the pull request comment. Continuing the example above, [Travis CI Build 80620536 ](https://travis-ci.org/travis-ci/apt-whitelist-checker/builds/80620536).

3. Search the build log for the phrase "Fetching source package for …" and expand the section.

4. Match that source against the `alias` name shown in
   [the source list](https://github.com/travis-ci/apt-source-whitelist/blob/master/ubuntu.json).

In our example, the source alias is "lucid":

```yaml
addons:
  apt:
    sources:
    - lucid
    packages:
    - libcxsparse3.1.2
```
{: data-file=".travis.yml"}

> If you require additional package sources, please use `sudo: required` in your `.travis.yml` file and install them manually. Unfortunately, we are unable to process [APT sources requests](https://github.com/travis-ci/apt-source-whitelist) at this time.

## Installing Packages on OS X

To install packages that are not included in the [default OS X environment](/user/reference/osx/#Compilers-and-Build-toolchain) use [Homebrew](http://brew.sh) in your `.travis.yml`. For example, to install beanstalk:

```yaml
before_install:
  - brew update # see note below
  - brew install beanstalk
```
{: data-file=".travis.yml"}

> To speed up your build, try installing your packages *without* running `brew update` first, to see if the Homebrew database on the build image already has what you need.

## Installing Dependencies on Multiple Operating Systems

If you're testing on both Linux and OS X, use the `$TRAVIS_OS_NAME` variable to install dependencies separately:

```yaml
install:
  - if [ $TRAVIS_OS_NAME = linux ]; then sudo apt-get install foo; else brew install bar; fi
```
{: data-file=".travis.yml"}

## Installing Projects from Source

Some dependencies can only be installed from a source package. The build may require a more recent version or a tool or library that's not available as a Ubuntu package.

You can easily include the build steps in either your .travis.yml or, and this is the recommended way, by running a script to handle the installation process.

Here's a simple example that installs CasperJS from a binary package:

```yaml
before_script:
  - wget https://github.com/n1k0/casperjs/archive/1.0.2.tar.gz -O /tmp/casper.tar.gz
  - tar -xvf /tmp/casper.tar.gz
  - export PATH=$PATH:$PWD/casperjs-1.0.2/bin/
```
{: data-file=".travis.yml"}

Note that when you're updating the `$PATH` environment variable, that part can't be moved into a shell script, as it will only update the variable for the sub-process that's running the script.

To install something from source, you can follow similar steps. Here's an example to download, compile and install the protobufs library.

```yaml
install:
  - wget https://protobuf.googlecode.com/files/protobuf-2.4.1.tar.gz
  - tar -xzvf protobuf-2.4.1.tar.gz
  - pushd protobuf-2.4.1 && ./configure --prefix=/usr && make && sudo make install && popd
```
{: data-file=".travis.yml"}

These three commands can be extracted into a shell script, let's name it `install-protobuf.sh`:

```bash
#!/bin/sh
set -ex
wget https://protobuf.googlecode.com/files/protobuf-2.4.1.tar.gz
tar -xzvf protobuf-2.4.1.tar.gz
cd protobuf-2.4.1 && ./configure --prefix=/usr && make && sudo make install
```

Once it's added to the repository, you can run it from your .travis.yml:

```yaml
before_install:
  - ./install-protobuf.sh
```
{: data-file=".travis.yml"}

Note that the first version uses `pushd` and `popd` to ensure that after the `install` section completes, the working directory is returned to its original value.  This is not necessary in the shell script, as it runs in a sub-shell and so does not alter the original working directory.