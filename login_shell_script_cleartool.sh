#!/bin/tcsh -f

echo "*** SELECT VIEW ***"
echo
set user = `/usr/ucb/whoami`
cleartool lsview | grep $user

#Taking user input
echo "Enter the view component: "
set req = $<

set viewname = $user"."$req

set TERM = xterm
set host = `hostname`
echo $host
echo $viewname
if ($host != lake) then
    cd /software/src/marlin
    setenv TERM xterm-256color
else
    cd /home/amajumda/cscope_92x
    echo
    echo "***Opening CSCOPE... Kindly use Ctrl+d to close CSCOPE instead of Ctrl+z...***"
    echo
    sleep 2
    cleartool setview -exec "cscope -d" $viewname
endif
echo
echo "################################################"
echo -n "Config spec of view: "
#cleartool setview -exec "catcs | sed -n 3p | awk '{print substr($2,25)}'" $viewname
cleartool setview -exec "catcs | sed -n 3p| cut -d ' ' -f2" $viewname
# Above might not always work, as the cs may not be the 6th element of splitted shit all the time...
#cleartool setview -exec "catcs | sed -n 3p" $viewname
sv -f $viewname
