{
 "cells": [
  {
   "attachments": {
    "image.png": {
     "image/png": "iVBORw0KGgoAAAANSUhEUgAADucAAACCCAYAAADvu/TPAAAgAElEQVR4Ae3bMREAAAgDMfybLhZeQJg75Vj/5ggQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQSAKXVkYECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECEyc6wkIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIRAFxboQyI0CAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQICDO9QMECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEooA4N0KZESBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIEBDn+gECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECUUCcG6HMCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECIhz/QABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgACBKCDOjVBmBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBMS5foAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIBAFBDnRigzAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAuJcP0CAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIEAgCohzI5QZAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAXGuHyBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECAQBcS5EcqMAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAgDjXDxAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBCIAuLcCGVGgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAQJzrBwgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAhEAXFuhDIjQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgIM71AwQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgSigDg3QpkRIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQEOf6AQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQJRQJwbocwIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIiHP9AAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAIEoIM6NUGYECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIExLl+gAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgEAUEOdGKDMCBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAEC4lw/QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQCAKiHMjlBkBAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABca4fIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIBAFxLkRyowAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQICAONcPECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIEIgC4twIZUaAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIEBAnOsHCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECEQBcW6EMiNAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECAgzvUDBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBKKAODdCmREgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAQ5/oBAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAlFAnBuhzAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAiIc/0AAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgSggzo1QZgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgTEuX6AAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAQBQQ50YoMwIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQLiXD9AgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAIAqIcyOUGQECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAFxrh8gQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgEAXEuRHKjAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgIA41w8QIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQiALi3AhlRoAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQECc6wcIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIRAFxboQyI0CAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQICDO9QMECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEooA4N0KZESBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIEBDn+gECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECUUCcG6HMCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECIhz/QABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgACBKCDOjVBmBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBMS5foAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIBAFBDnRigzAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAuJcP0CAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIEAgCohzI5QZAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAXGuHyBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECAQBcS5EcqMAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAgDjXDxAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBCIAuLcCGVGgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAQJzrBwgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAhEAXFuhDIjQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgIM71AwQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgSigDg3QpkRIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQEOf6AQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQJRQJwbocwIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIiHP9AAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAIEoIM6NUGYECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIExLl+gAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgEAUEOdGKDMCBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAEC4lw/QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQCAKiHMjlBkBAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABca4fIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIBAFxLkRyowAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQICAONcPECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIEIgC4twIZUaAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIEBAnOsHCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECEQBcW6EMiNAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECAgzvUDBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBKKAODdCmREgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAQ5/oBAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAlFAnBuhzAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAiIc/0AAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgSggzo1QZgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgTEuX6AAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAQBQQ50YoMwIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQLiXD9AgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAIAqIcyOUGQECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAFxrh8gQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgEAXEuRHKjAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgIA41w8QIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQiALi3AhlRoAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQECc6wcIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIRAFxboQyI0CAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQICDO9QMECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEooA4N0KZESBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIEBDn+gECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECUUCcG6HMCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECIhz/QABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgACBKCDOjVBmBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBMS5foAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIBAFBDnRigzAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAuJcP0CAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIEAgCohzI5QZAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAXGuHyBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECAQBcS5EcqMAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAgDjXDxAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBCIAuLcCGVGgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAQJzrBwgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAhEAXFuhDIjQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgIM71AwQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgSigDg3QpkRIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQEOf6AQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQMhOevIAAAMcSURBVIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQJRQJwbocwIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIiHP9AAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAIEoIM6NUGYECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIExLl+gAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgEAUEOdGKDMCBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAEC4lw/QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQCAKiHMjlBkBAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABca4fIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIBAFxLkRyowAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQICAONcPECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIECBAgAABAgQIEIgC4twIZUaAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIECAAAECBAgQIEDgARDZtyFBv0bZAAAAAElFTkSuQmCC"
    }
   },
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Projeto - Análise e Visualização de Dados\n",
    "\n",
    "Em nossas aulas, conhecemos as principais bibliotecas para se trabalhar com Análise e Visualização de Dados em Python. Aprendemos também como trabalhar com tabelas e fazer operações sobre elas, de modo que possamos analisar e inferir sobre uma base de dados existente.\n",
    "\n",
    "Para este projeto, imagine que o seu chefe disponibilize uma base de dados para que você possa analisá-la a partir dos seus conhecimentos em Python. Para essa tarefa, você deve utilizar o Matplotlib para visualização de alguns gráficos e demais bibliotecas, Pandas e NumPy para análise e manipulação dos dados. Com o correto uso das funcionalidades da linguagem, você será capaz de conduzir de maneira correta, a análise e visualização de dados, trabalho básico de um Cientista de Dados.\n",
    "Para iniciar o seu projeto, siga as instruções abaixo:\n",
    "\n",
    "* Faça o download dos arquivos disponibilizados nesta aula e armazene na mesma pasta em que irá armazenar os seus arquivos de código.\n",
    "* Carregue a tabela .csv para que você possa fazer a leitura de dados da mesma\n",
    "* Imprima parte do conteúdo para verificar se a leitura está acontecendo corretamente\n",
    "![image.png](attachment:image.png)\n",
    "\n",
    "**Obs: Nessa primeira etapa, indicada pelas instruções acima, eu já te ajudei, indicando o caminho para carregar a tabela, conforme código abaixo :D #ThanksGod**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Gestor</th>\n",
       "      <th>Canal de Origem</th>\n",
       "      <th>Região</th>\n",
       "      <th>UF</th>\n",
       "      <th>Cidade</th>\n",
       "      <th>Sexo</th>\n",
       "      <th>Faixa Etária</th>\n",
       "      <th>Ano Abertura</th>\n",
       "      <th>Mês Abertura</th>\n",
       "      <th>Data Abertura</th>\n",
       "      <th>...</th>\n",
       "      <th>Como Comprou Contratou</th>\n",
       "      <th>Procurou Empresa</th>\n",
       "      <th>Respondida</th>\n",
       "      <th>Situação</th>\n",
       "      <th>Avaliação Reclamação</th>\n",
       "      <th>Nota do Consumidor</th>\n",
       "      <th>Análise da Recusa</th>\n",
       "      <th>Edição de Conteúdo</th>\n",
       "      <th>Interação do Gestor</th>\n",
       "      <th>Total</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Secretaria Nacional do Consumidor</td>\n",
       "      <td>Não identificado</td>\n",
       "      <td>SE</td>\n",
       "      <td>RJ</td>\n",
       "      <td>Itaboraí</td>\n",
       "      <td>M</td>\n",
       "      <td>entre 31 a 40 anos</td>\n",
       "      <td>2014</td>\n",
       "      <td>6</td>\n",
       "      <td>27/06/2014</td>\n",
       "      <td>...</td>\n",
       "      <td>Não comprei / contratei</td>\n",
       "      <td>S</td>\n",
       "      <td>S</td>\n",
       "      <td>Finalizada não avaliada</td>\n",
       "      <td>Não Avaliada</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>N</td>\n",
       "      <td>N</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Instituto Estadual de Proteção e Defesa do Con...</td>\n",
       "      <td>Não identificado</td>\n",
       "      <td>SE</td>\n",
       "      <td>ES</td>\n",
       "      <td>Serra</td>\n",
       "      <td>F</td>\n",
       "      <td>entre 31 a 40 anos</td>\n",
       "      <td>2014</td>\n",
       "      <td>6</td>\n",
       "      <td>11/06/2014</td>\n",
       "      <td>...</td>\n",
       "      <td>Internet</td>\n",
       "      <td>S</td>\n",
       "      <td>S</td>\n",
       "      <td>Finalizada avaliada</td>\n",
       "      <td>Não Resolvida</td>\n",
       "      <td>1.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>N</td>\n",
       "      <td>N</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Secretaria Nacional do Consumidor</td>\n",
       "      <td>Não identificado</td>\n",
       "      <td>SE</td>\n",
       "      <td>RJ</td>\n",
       "      <td>Volta Redonda</td>\n",
       "      <td>M</td>\n",
       "      <td>entre 31 a 40 anos</td>\n",
       "      <td>2014</td>\n",
       "      <td>6</td>\n",
       "      <td>27/06/2014</td>\n",
       "      <td>...</td>\n",
       "      <td>Internet</td>\n",
       "      <td>S</td>\n",
       "      <td>S</td>\n",
       "      <td>Finalizada avaliada</td>\n",
       "      <td>Resolvida</td>\n",
       "      <td>5.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>N</td>\n",
       "      <td>N</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Instituto de Promoção e Defesa do Cidadão e Co...</td>\n",
       "      <td>Não identificado</td>\n",
       "      <td>NE</td>\n",
       "      <td>MA</td>\n",
       "      <td>São Luís</td>\n",
       "      <td>F</td>\n",
       "      <td>entre 31 a 40 anos</td>\n",
       "      <td>2014</td>\n",
       "      <td>5</td>\n",
       "      <td>29/05/2014</td>\n",
       "      <td>...</td>\n",
       "      <td>Não comprei / contratei</td>\n",
       "      <td>S</td>\n",
       "      <td>S</td>\n",
       "      <td>Finalizada avaliada</td>\n",
       "      <td>Resolvida</td>\n",
       "      <td>5.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>N</td>\n",
       "      <td>N</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Secretaria de Desenvolvimento Social e Direito...</td>\n",
       "      <td>Não identificado</td>\n",
       "      <td>NE</td>\n",
       "      <td>PE</td>\n",
       "      <td>Recife</td>\n",
       "      <td>M</td>\n",
       "      <td>entre 21 a 30 anos</td>\n",
       "      <td>2014</td>\n",
       "      <td>6</td>\n",
       "      <td>30/06/2014</td>\n",
       "      <td>...</td>\n",
       "      <td>Internet</td>\n",
       "      <td>S</td>\n",
       "      <td>S</td>\n",
       "      <td>Finalizada não avaliada</td>\n",
       "      <td>Não Avaliada</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>N</td>\n",
       "      <td>N</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 38 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                              Gestor   Canal de Origem Região  \\\n",
       "0                  Secretaria Nacional do Consumidor  Não identificado     SE   \n",
       "1  Instituto Estadual de Proteção e Defesa do Con...  Não identificado     SE   \n",
       "2                  Secretaria Nacional do Consumidor  Não identificado     SE   \n",
       "3  Instituto de Promoção e Defesa do Cidadão e Co...  Não identificado     NE   \n",
       "4  Secretaria de Desenvolvimento Social e Direito...  Não identificado     NE   \n",
       "\n",
       "   UF         Cidade Sexo        Faixa Etária  Ano Abertura  Mês Abertura  \\\n",
       "0  RJ       Itaboraí    M  entre 31 a 40 anos          2014             6   \n",
       "1  ES          Serra    F  entre 31 a 40 anos          2014             6   \n",
       "2  RJ  Volta Redonda    M  entre 31 a 40 anos          2014             6   \n",
       "3  MA       São Luís    F  entre 31 a 40 anos          2014             5   \n",
       "4  PE         Recife    M  entre 21 a 30 anos          2014             6   \n",
       "\n",
       "  Data Abertura  ...   Como Comprou Contratou Procurou Empresa Respondida  \\\n",
       "0    27/06/2014  ...  Não comprei / contratei                S          S   \n",
       "1    11/06/2014  ...                 Internet                S          S   \n",
       "2    27/06/2014  ...                 Internet                S          S   \n",
       "3    29/05/2014  ...  Não comprei / contratei                S          S   \n",
       "4    30/06/2014  ...                 Internet                S          S   \n",
       "\n",
       "                  Situação Avaliação Reclamação Nota do Consumidor  \\\n",
       "0  Finalizada não avaliada         Não Avaliada                NaN   \n",
       "1      Finalizada avaliada        Não Resolvida                1.0   \n",
       "2      Finalizada avaliada            Resolvida                5.0   \n",
       "3      Finalizada avaliada            Resolvida                5.0   \n",
       "4  Finalizada não avaliada         Não Avaliada                NaN   \n",
       "\n",
       "  Análise da Recusa Edição de Conteúdo Interação do Gestor Total  \n",
       "0               NaN                  N                   N     1  \n",
       "1               NaN                  N                   N     1  \n",
       "2               NaN                  N                   N     1  \n",
       "3               NaN                  N                   N     1  \n",
       "4               NaN                  N                   N     1  \n",
       "\n",
       "[5 rows x 38 columns]"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# importa a biblioteca pandas\n",
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv(\"dadosgovbr---2014.csv\",sep = ';', encoding=\"latin-1\")\n",
    "# visualizar alguns dados da tabela carregada\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Aí vai uma dica preciosa: Para responder questões relacionadas a frequência de ocorrências, como exemplo, você pode testar o comando a seguir:\n",
    "         \n",
    "         df.Região.value_counts()\n",
    "         \n",
    "O código acima retorna a quantidade de ocorrências de registros de uma determinada região. Use essa lógica quando necessário.\n",
    "Em relação as demais questões, consulte diversas fontes, caso necessário, para responder corretamente. Dessa forma, tendo como base o data frame em questão, responda as questões relacionadas:\n",
    "\n",
    "### Análise de Dados\n",
    "\n",
    "1. Qual a quantidade de reclamações registradas?\n",
    "2. Qual é o tempo médio, máximo e mínimo de resposta?\n",
    "3. Qual é a nota média, máxima e mínima do consumidor?\n",
    "4. Como podemos correlacionar a nota do consumidor com o tempo de resposta? Explique.\n",
    "5. Qual a quantidade de reclamações por Sexo?\n",
    "6. Qual a quantidade de reclamações por Estado?\n",
    "4. Qual é a porcentagem de reclamações registradas e não respondidas?\n",
    "\n",
    "### Visualização de Dados\n",
    "\n",
    "Neste momento iremos trabalhar com visualização de dados. Antes de iniciar a impressão dos gráficos, trate de fazer as configurações iniciais para que a impressão ocorra no Jupyter de maneira correta e com todos os requisitos necessários para melhoria da apresentação como um todo. Faça o melhor possível, como se fosse apresentar para o seu chefe. Siga as instruções a seguir:\n",
    "\n",
    "5. Gere um gráfico com titulo, nome dos eixos, cor e legenda para as seguintes situações:\n",
    "   * a) Frequência de reclamações por sexo\n",
    "   * b) Frequencia de reclamações por estado\n",
    "   * c) Frequência de reclamações respondidas e não respondidas\n",
    "6. Imagine que você é um Cientista de Dados responsável por medir a satisfação dos clientes. Para que você possa surpreender seu chefe, você deve fazer duas análises importantes sobre o data frame, incluindo no mínimo dois gráficos com suas devidas personalizações de titulo, nome dos eixos, legenda, estilos etc. Considere que, ao trazer informações relevantes para a empresa em que trabalha, mais chances de ter o seu trabalho reconhecido e de ser um profissional com maior valor no mercado. Capriche nos gráficos!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Análise de Dados"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "43987\n"
     ]
    }
   ],
   "source": [
    "# 1. Qual a quantidade de reclamações registradas?\n",
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv(\"dadosgovbr---2014.csv\",sep = ';', encoding=\"latin-1\")\n",
    "rec = df[\"Total\"].sum()\n",
    "print(rec)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tempo mínimo: 1 \n",
      " Tempo médio: 1.0 \n",
      " Tempo máximo: 1 \n",
      "\n"
     ]
    }
   ],
   "source": [
    "# 2. Qual é o tempo médio, máximo e mínimo de resposta?\n",
    "\n",
    "\n",
    "# deltaT mínimo:\n",
    "delta_min = df[\"Total\"].min()\n",
    "\n",
    "# deltaT medio: \n",
    "delta_mean = df[\"Total\"].mean()\n",
    "\n",
    "# deltaT máximo: \n",
    "delta_max = df[\"Total\"].max()\n",
    "\n",
    "print(\"Tempo mínimo: {} \\n\".format(delta_min),\n",
    "      \"Tempo médio: {} \\n\".format(delta_mean),\n",
    "      \"Tempo máximo: {} \\n\".format(delta_max)\n",
    ")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nota mínima: 1.0 \n",
      " Nota média: 3.007021343486918 \n",
      " Nota máxima: 5.0 \n",
      "\n"
     ]
    }
   ],
   "source": [
    "# 3. Qual é a nota média, máxima e mínima do consumidor?\n",
    "\n",
    "# nota média:\n",
    "nota1 = df[\"Nota do Consumidor\"].min()\n",
    "nota2 = df[\"Nota do Consumidor\"].mean()\n",
    "nota3 = df[\"Nota do Consumidor\"].max()\n",
    "\n",
    "print(\"Nota mínima: {} \\n\".format(nota1),\n",
    "      \"Nota média: {} \\n\".format(nota2),\n",
    "      \"Nota máxima: {} \\n\".format(nota3)\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 4. Como podemos correlacionar a nota do consumidor com o tempo de resposta? Explique.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "M    27895\n",
      "F    16092\n",
      "Name: Sexo, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# 5. Qual a quantidade de reclamações por Sexo?\n",
    "quant = df['Sexo'].value_counts(dropna=True)\n",
    "\n",
    "print(quant)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "SP    11882\n",
      "PR     6140\n",
      "RJ     4907\n",
      "MG     4186\n",
      "BA     2443\n",
      "RS     1941\n",
      "DF     1805\n",
      "PE     1626\n",
      "SC     1458\n",
      "MA     1082\n",
      "ES     1081\n",
      "CE     1068\n",
      "MT     1012\n",
      "GO      886\n",
      "MS      531\n",
      "AC      449\n",
      "PB      343\n",
      "AM      291\n",
      "PA      211\n",
      "RN      160\n",
      "RO      119\n",
      "AL      104\n",
      "SE       97\n",
      "PI       77\n",
      "TO       46\n",
      "RR       24\n",
      "AP       18\n",
      "Name: UF, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# 6. Qual a quantidade de reclamações por Estado?\n",
    "\n",
    "quant = df['UF'].value_counts(dropna=True)\n",
    "\n",
    "print(quant)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "S    95.394094\n",
      "N     4.605906\n",
      "Name: Respondida, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# 7. Qual é a porcentagem de reclamações registradas e não respondidas?\n",
    "# resol = \n",
    "\n",
    "# print(rec)\n",
    "\n",
    "# resol = df['Respondida'].value_counts()\n",
    "rec_total = df[\"Total\"].sum()\n",
    "rec_nao_resol = df[\"Respondida\"].value_counts()\n",
    "porcentagem = (rec_nao_resol / rec_total) * 100\n",
    "\n",
    "print(porcentagem)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Visualização de Dados"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 1a) Gere um gráfico com titulo, nome dos eixos, cor e legenda para as seguintes situações:\n",
    "# a) Frequência de reclamações por sexo\n",
    "\n",
    "import matplotlib.pyplot as plt \n",
    "\n",
    "labels = 'Mulheres', 'Homens'\n",
    "sizes = [16092, 27895]\n",
    "\n",
    "fig1, ax1 = plt.subplots()\n",
    "ax1.pie(sizes, labels=labels, autopct='%1.1f%%',\n",
    "        shadow=True, startangle=90, colors=['red','pink'])\n",
    "ax1.axis('equal')  \n",
    "\n",
    "plt.savefig('pie_chart.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'Número de Reclamações')"
      ]
     },
     "execution_count": 176,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 1b) Frequencia de reclamações por estado\n",
    "import matplotlib.pyplot as plt \n",
    "\n",
    "\n",
    "df[\"UF\"].value_counts().plot.bar()\n",
    "plt.title('Relação entre o número de reclamções e Unidades da Federeção')\n",
    "plt.xlabel('Unidades Federativas')\n",
    "plt.ylabel('Número de Reclamações')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 194,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# 1c) Frequência de reclamações respondidas e não respondidas\n",
    "\n",
    "\n",
    "rec_total = df[\"Total\"].sum()\n",
    "rec_nao_resol = df[\"Respondida\"].value_counts()\n",
    "porcentagem = (rec_nao_resol / rec_total) * 100\n",
    "sizes = ['2026','43957']\n",
    "\n",
    "fig1, ax1 = plt.subplots()\n",
    "ax1.pie(sizes, labels=labels, autopct='%1.1f%%',\n",
    "        shadow=True, startangle=90, colors=['red','pink'])\n",
    "ax1.axis('equal') \n",
    "\n",
    "plt.savefig('pie_chart.png')\n",
    "plt.show()\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. você deve fazer duas análises importantes sobre o data frame, incluindo no mínimo dois gráficos com suas devidas personalizações de titulo, nome dos eixos, legenda, estilos etc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "labels = 'Clientes que procuraram a empresa', 'Clientes que não procuraram a empresa'\n",
    "\n",
    "rec_total = df['Total'].sum()\n",
    "rec_nao_resol = df['Procurou Empresa'].value_counts()\n",
    "sizes = ['40066', '3921']\n",
    "\n",
    "fig1, ax1 = plt.subplots()\n",
    "ax1.pie(sizes, labels=labels, autopct='%1.1f%%',\n",
    "        shadow=False, startangle=90, colors=['green','gray'])\n",
    "ax1.axis('equal') \n",
    "\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 199,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "labels = 'Procedente', 'Improcedente', 'Encerrada'\n",
    "\n",
    "rec_total = df['Total'].sum()\n",
    "rec_nao_resol = df['Análise da Recusa'].value_counts()\n",
    "sizes = ['1662', '291', '93']\n",
    "\n",
    "fig1, ax1 = plt.subplots()\n",
    "ax1.pie(sizes, labels=labels, autopct='%1.1f%%',\n",
    "        shadow=False, startangle=90, colors=['green','gray', 'orange'])\n",
    "ax1.axis('equal') \n",
    "\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
