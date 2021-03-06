# WPI XC/TF Schedule Tracker

## Impetus

This project was developed as a replacement for a scheduling utility developed by a former student at WPI and athlete on the Track and Field team. Its primary use case was for coaches to aggregate schedule data to plan meetings with their various student athletes. The previous site had critical security flaws and some design issues that made it difficult to debug. To give the original developer the benefit of the doubt, they did make it as a school project.

I am developing this website as an overall improvement to the previous implementation. This is the minimum product:

* Secure API
* Schedule aggregation by major
* Schedule aggregation by event group
* Schedule spreadsheet export
* Multi-add course form
* Profile forms (event and year info)
* All WPI official Degrees and Certificates
* Admin panel for easy administration

## Future plans

The design of this site is basic to start but there are many possibilities for how it can be improved and extended. The running list of ideas are as follows:

* Top 10 performances list (per event, per gender)
* Calls to TFRRS API or webcrawling for updated top 10 performances
* Training plan builder (with excel export)
* Microsoft login strategy for easy auth
