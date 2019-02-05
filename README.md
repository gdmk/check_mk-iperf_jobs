This check measures and checks Iperf3 based network tests. This check relies on a mk_iperf_jobs plugin (comes with this check),
 which should be deployed on the actual PC/server that initiates the tests. Since multiple Iperf checks can be specified and run at the same time
 the mk_iperf_jobs forks and runs parallel processes decreasing the overall run time which will be equal to the longest check. However, despite this fact it is still
 preferrable to run the mk_iperf_jobs in async mode (create a folder in plugins directory which name is amount of seconds as the run interval).
 Make sure to set the timeout in global_set of the iperf_jobs.cfg config to the longest test in 'servers' of the config (in duration attribute). Keep in mind that test 
 runs in both directions, so if you set duration to 5 sec, the test will run 5 sec to destination, then destination originates another test back to source, which is
 another 5 sec, so the total test duration is 10 sec. If the test runs over the global_set[timeout], it will be SIGTERM with UNKNOWN check result. 

 Note: the mk_iperf_jobs has several dependencies, the PC/server has to have the actual binary Iperf3 installed, version 3.1 or better (provides built-in libiperf API),
 the python wrapper for iperf3 from https://iperf3-python.readthedocs.io/en/latest/ (can be installed via PIP)
 
 Should work with Iperf3 3.(1-6), however this mostly depends on compatibility with API wrapper above
 
 Will work with Check_MK version 1.2.8 (will use PNP4Nagios generic template) to 1.5 (will use new metrics def for either PNP4Nagios or HTML5 based for CEE edition), CMC or Nagios
