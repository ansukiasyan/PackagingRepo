# BUILD stage
FROM centos:7 as BUILD

WORKDIR /build
COPY ./patch.diff ./patch.diff

RUN yum install -y \
    patch \
    make \
    gcc \
    rpm-build \
    rpmdevtools \
    pam-devel \
    libcap-devel \
    openssl-devel \
    tcp_wrappers-devel

ADD http://vault.centos.org/7.7.1908/os/Source/SPackages/vsftpd-3.0.2-25.el7.src.rpm vsftpd-3.0.2-25.el7.src.rpm
RUN rpm -Uv ./vsftpd-3.0.2-25.el7.src.rpm

RUN cd /root/rpmbuild/SPECS \
    && patch -p0 < /build/patch.diff \
    && cd /root/rpmbuild \
    && rpmbuild -ba SPECS/vsftpd.spec

# TEST Stage
FROM centos:7 as TEST

RUN yum install -y logrotate 
COPY --from=BUILD /root/rpmbuild/RPMS/x86_64/vsftpd-3.0.2-25.el7.x86_64.rpm /vsftpd-3.0.2-25.el7.x86_64.rpm
RUN rpm -Uv /vsftpd-3.0.2-25.el7.x86_64.rpm

CMD ["cp", "/vsftpd-3.0.2-25.el7.x86_64.rpm", "/output"]

# docker build -t rpm-build .
# docker run -t --rm -v $(pwd):/output:rw rpm-build
