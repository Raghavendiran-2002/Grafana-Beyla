# Grafana Beyla Flask Observability Demo

## 📦 Stack Components

- Flask Python app (with gunicorn)
- Grafana Beyla (eBPF mode)
- Prometheus
- Tempo
- Grafana

## ▶️ Run the Stack

Verify eBPF is supported on linux kernal :

```bash
docker info | grep Kernel
```

Ensure the printed version is **4.9 or later**


Enable eBPF Support on container

```bash
bpftool feature
```

```bash
docker-compose up --build
```

## 🔗 Access

- Flask App: http://localhost:8000
- Status: http://localhost:8000/status
- Grafana: http://localhost:3000 (admin/admin)
- Add "Data Source" -> "prometheus" -> set "prometheus server URL" =  "http://prometheus:9090"
- Prometheus: http://localhost:9090
- Tempo (via Grafana Explore)

## 🧪 Test Endpoints

```bash
curl http://localhost:8000/
curl http://localhost:8000/status
```

## 🧹 Cleanup

```bash
docker-compose down
```

Ensure Docker is running on a Linux-based host with `x86_64` architecture and that you have permissions to run containers with `SYS_ADMIN` capability.
