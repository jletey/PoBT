#!/usr/bin/env bash
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# title      Run Script                                                            +
# project    A-Study-of-Transcription-and-Its-Affects                              +
# repository https://github.com/johnletey/A-Study-of-Transcription-and-Its-Affects +
# author     John Letey                                                            +
# email      john.letey@colorado.edu                                               +
# copyright  Copyright (C) 2018                                                    +
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
set -e

_ct_error="\e[0;31m"
_ct_success="\e[0;32m"
_ct_warning="\e[0;33m"
_ct_highlight="\e[0;34m"
_ct_primary="\e[0;36m"
_ct="\e[0;37m"
_ctb_subtle="\e[1;30m"
_ctb_error="\e[1;31m"
_ctb_success="\e[1;32m"
_ctb_warning="\e[1;33m"
_ctb_highlight="\e[1;34m"
_ctb_primary="\e[1;36m"
_ctb="\e[1;37m"
_c_reset="\e[0m"

__help() {
  printf "${_ctb}Usage: ${_ct_primary}run.sh ${_ctb_subtle}[OPTIONS]\n"
  printf "  ${_ctb_highlight}-h${_ct},${_ctb_highlight} --help                             ${_ct}Help\n${_ctb_reset}"
  printf "  ${_ctb_highlight}-r${_ct},${_ctb_highlight} --requirements <REQUIREMENTS FILE> ${_ct}Install the project requirements\n${_ctb_reset}"
  printf "  ${_ctb_highlight}-v${_ct},${_ctb_highlight} --verbose                          ${_ct}Verbose output\n${_ctb_reset}"
}

__cleanup() {
  trap '' SIGINT SIGTERM
  unset -v _ct_error _ct_success _ct_warning _ct_highlight _ct_primary _ct
  unset -v _ctb_error _ctb_success _ctb_warning _ctb_highlight _ctb_primary _ctb _c_reset
  unset -v SCRIPT_OPTS COLOR_THEME_FILE VERBOSE LOCAL_INSTALL NORD_DIRCOLORS_VERSION
  unset -f __help __cleanup __log_error __log_success __log_warning __log_info
  unset -f __validate_file __local_install __global_install
}

__log_error() {
  printf "${_ctb_error}[ERROR] ${_ct}$1${_c_reset}\n"
}

__log_success() {
  printf "${_ctb_success}[OK] ${_ct}$1${_c_reset}\n"
}

__log_warning() {
  printf "${_ctb_warning}[WARN] ${_ct}$1${_c_reset}\n"
}

__log_info() {
  printf "${_ctb_subtle}[INFO] ${_ct}$1${_c_reset}\n"
}

__summary_success() {
  __log_success "Local installation completed"
  __cleanup
  exit 0
}

__summary_error() {
  __log_error
  __log_error "Exit code: $1"
  __cleanup
  exit 1
}

__summary_validation_error() {
  __log_error "An error occurred when trying to validate file!"
  __log_error "Exit code: $1"
  __cleanup
  exit 1
}

__install_requirements() {
    __log_info "Checking to see if the requirements file is valid"    
    __validate_file
    __log_info "Installing the project requirements"
    pip install -q -r $REQUIREMENTS_FILE
    # pip3 install -q -r $REQUIREMENTS_FILE
}

__validate_file() {
  if [ ! -f $REQUIREMENTS_FILE ]; then
    __log_error "Requirements file not found: $REQUIREMENTS_FILE"
    __summary_validation_error 1
  else
    __log_success "Requirements file found: $REQUIREMENTS_FILE"
  fi
}

trap "printf '${_ctb_error}User aborted.${_ctb_reset}\n' && exit 1" SIGINT SIGTERM

SCRIPT_OPTS=`getopt -o vhc: --long verbose,help,requirementsfile: -n 'run.sh' -- "$@"`
REQUIREMENTS_FILE=requirements.txt
VERBOSE=false

eval set -- "$SCRIPT_OPTS"
while true; do
  case "$1" in
    -v | --verbose ) VERBOSE=true; shift ;;
    -h | --help ) __help; exit 0; break ;;
    -r | --requirements )
      REQUIREMENTS_FILE="$2"; shift 2 ;;
    -- ) shift; break ;;
    * ) break ;;
  esac
done

__install_requirements
__cleanup
exit 0