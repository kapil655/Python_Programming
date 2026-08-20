import speedtest

st = speedtest.Speedtest()
st.get_best_server()

print(f"download: {st.download() / 1_000_000:.2f} Mbps")
print(f"Upload: {st.upload() / 1_000_000:.2f} Mbps")
print(f"ping :{st.results.ping} ms")
