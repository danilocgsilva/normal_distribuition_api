# Normal distribuition api

Provide a json string, return a set of values, which obeys the normal distribution pattern, right from localhost. So, after rising up the container, just access in the browser (or some api client) the address: `http://localhost:5000`.

Just ensure that the port 5000 is not currently uses. If so, just change the CMD Dockerfile to alter the port.

You can provide a query parameter called `count`, so you can control the amount of values given. Eg.: `http://localhost:5000?count=50`.

