# !/bin/sh

RTE_SDK="/root/dpdk"
RTE_TARGET="x86_64-native-linuxapp-gcc"
RTE_IGB_UIO="/root/dpdk/x86_64-native-linuxapp-gcc/kernel/linux/igb_uio"
RTE_KNI="/root/dpdk/x86_64-native-linuxapp-gcc/kernel/linux/kni"
RTE_DEV_TOOL="$RTE_SDK/usertools/dpdk-devbind.py "

# this is dpdk setup in vmware

# compile dpdk
cd $RTE_SDK
rm -rf $RTE_TARGET
meson -Dexamples=all -Denable_kmods=true $RTE_TARGET
cd $RTE_TARGET
ninja
ninja install
ldconfig
cd ~

# insmod dpdk uio
cd $RTE_IGB_UIO
rmmod igb_uio.ko
modprobe uio
insmod igb_uio.ko
cd ~

cd $RTE_KNI
rmmod rte_kni.ko
insmod rte_kni.ko kthread_mode=multiple
cd ~

# eth down
ifconfig ens38 down > /dev/null 2>&1
ifconfig ens39 down > /dev/null 2>&1
ifconfig ens40 down > /dev/null 2>&1
ifconfig ens41 down > /dev/null 2>&1

# sleep 3 seconds
sleep 3

# bind network device

# second bind
eval  python3 $RTE_DEV_TOOL "-b igb_uio 0000:02:06.0 0000:02:07.0 0000:02:08.0 0000:02:09.0"

echo "\n======== after dev bind========\n"
eval python3 $RTE_DEV_TOOL "--status"
