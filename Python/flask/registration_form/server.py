from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile
