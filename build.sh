# 단일 아키텍처 Docker build 명령어. 현재는 주석 처리되어 있습니다.
# docker build -t nineking424/pybitmex .

# Docker buildx를 사용하기 위해 빌더를 생성합니다.(optional)
# docker buildx create --name cross-platform-builder --driver docker-container --use

# Docker buildx를 사용하여 멀티 플랫폼 이미지를 빌드합니다.
# -t 옵션은 생성될 Docker 이미지의 이름을 지정합니다.
# --platform 옵션은 이미지를 빌드할 대상 플랫폼을 지정합니다.
# --push 옵션은 빌드가 완료된 후 이미지를 Docker Hub에 푸시합니다.
docker buildx build -t nineking424/pybitmex:latest --platform=linux/amd64,linux/arm64 --push .

# Docker compose를 사용하여 컨테이너를 실행합니다.
# docker compose -f docker-compose.yaml up
# docker compose -f docker-compose-local.yaml up
# docker compose -f docker-compose-all.yaml up