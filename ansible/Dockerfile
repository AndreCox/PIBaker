FROM alpine:3.7

ENV ANSIBLE_VERSION=2.9.9

ENV BUILD_PACKAGES \
        bash \
        curl \
        tar \
        nano \
        openssh-client \
        sshpass \
        git \
        python \
        py-boto \
        py-dateutil \
        py-httplib2 \
        py-jinja2 \
        py-paramiko \
        py-pip \
        py-setuptools \
        py-yaml \
        ca-certificates

RUN apk --update add --virtual build-dependencies \
        gcc \
        musl-dev \
        libffi-dev \
        openssl-dev \
        python-dev && \
    set -x && \
    apk update && apk upgrade && \
    apk add --no-cache ${BUILD_PACKAGES} && \
    pip install --upgrade pip && \
    pip install python-keyczar docker-py boto3 botocore && \
    apk del build-dependencies && \
    rm -rf /var/cache/apk/* && \
    mkdir -p /etc/ansible/ /ansible && \
    echo "[local]" >> /etc/ansible/hosts && \
    echo "localhost" >> /etc/ansible/hosts && \
    curl -fsSL https://releases.ansible.com/ansible/ansible-${ANSIBLE_VERSION}.tar.gz -o ansible.tar.gz && \
    tar -xzf ansible.tar.gz -C /ansible --strip-components 1 && \
    rm -fr ansible.tar.gz /ansible/docs /ansible/examples /ansible/packaging

ENV ANSIBLE_GATHERING=smart \
    ANSIBLE_HOST_KEY_CHECKING=false \
    ANSIBLE_RETRY_FILES_ENABLED=false \
    ANSIBLE_ROLES_PATH=/ansible/playbooks/roles \
    ANSIBLE_SSH_PIPELINING=True \
    PYTHONPATH=/ansible/lib \
    PATH=/ansible/bin:$PATH \
    ANSIBLE_LIBRARY=/ansible/library \
    EDITOR=nano

WORKDIR /ansible/playbooks

ENTRYPOINT ["ansible-playbook"]