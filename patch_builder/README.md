
## Build Patch
```
docker build -t rpm-build-patch -f Dockerfile.createpatch .
docker run -t --rm -v $(pwd):/output:rw rpm-build-patch
```
as a result you will get patch.diff in the current directory.