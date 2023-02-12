import streamlit as st
import streamlit.components.v1 as com

#1. use markdown (unofficial)
#2. html function of the component module of streamlit (official)

htmlcode= """
<div>
    <H1> This is my heading </H1>
    <p>
        The Teams page contains a listing of the various Community Teams, their responsibilities, links to their Wiki Home Pages and leaders, communication tools, and a quick reference to let you know whether and when they hold meetings.

Most Teams. Wiki Home Pages provide information about who they are, what they do, when their meetings are, and how to contact them. Using these pages, teammates are able to communicate and coordinate projects.
    </p>
</div>
"""
com.html(htmlcode)
