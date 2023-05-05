# Video Streaming Appplication

### How to run

- First, open new terminal as a server side<br>
- Enter command below<br>
```python
python Server.py <server_port>
```

<server_port> is a port to help Server create RTSP connecion.
Standar for port is 554, but is this case, we need more large than 1024.<br>
- Now, open a second terminal as a client side
- Enter command below<br>
```python
python ClientLauncher.py <server_host> <server_port> <rtp_port> <video_file>
```
<server_host> : your IP address <br>
<server_port> : the port that you used in the server side <br>
<rtp_port> : port to receive RTP packet (any integer number > 0 that you want) <br>
<video_file> : name of video that you want to stream (in this assignment video_file is movie.Mjpeg)
