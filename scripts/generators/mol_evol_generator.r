############################################################
# For rodent web, 01.20
# This generates the file "mol_evol.html"
############################################################


cat("Rendering mol_evol.rmd/html\n")
Sys.setenv(RSTUDIO_PANDOC="C:/Program Files/RStudio/bin/pandoc/")
library(rmarkdown)
setwd("C:/bin/hamster-genome/scripts/generators")
output_dir = "../.."
render("../markdown/mol_evol.rmd", output_dir = output_dir, params = list(output_dir = output_dir), quiet = TRUE)