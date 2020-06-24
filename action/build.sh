#!/bin/bash

echo "hello $1"
time=$(date)

ls -lah

echo "Home"
ls -l /github/home

echo "Workflow"
ls -l /github/workflow

echo "Workspace"
ls -l /github/workspace

echo "PWD"
pwd

echo "::set-output name=time::$time"
