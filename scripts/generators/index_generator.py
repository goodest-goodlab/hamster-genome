############################################################
# For ConGen2020 site, 08.20
# This generates the file "index.html"
############################################################

import sys, os
sys.path.append('..')
import lib.read_chunks as RC

######################
# HTML template
######################

html_template = """
<!doctype html>
    {head}

<body>
    <div class="row" id="header">Phodopus genome resources</div>
    {nav}

    <div class="row" id="sep_div"></div>
    <div class="row" id="img-row">
        <div class="col-8-24" id="margin"></div>
        <div class="col-8-24" id="img-col">
            <img id="res-img" src="img/phodopus.jpg">
            <center><span class="fig-caption"><a href="https://www.zoologie.uni-halle.de/im/1255694453_490_00_800.jpg" target="_blank">Source</a></a></span></center>
        </div>
        <div class="col-8-24" id="margin"></div>
    </div>
    <div class="row" id="sep_div"></div>

    {footer}

</body>
</html>
"""

######################
# Main block
######################
pagefile = "index.html";
print("Generating " + pagefile + "...");
title = "Phodopus"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));