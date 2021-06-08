#! /bin/sh

# this is auto config for ubuntu

host_file="/etc/hosts"

echo "this script install everything lee needed in ubuntu"
echo "required root user"
read -p "Are you sure [Y/n]: " sure
case $sure in
    [yY][eE][sS]|[yY])
        echo "install will take a very long time, have a coffee ..."
        ;;
    [nN][oO]|[nN])
        echo "see you again ^_^ "
        exit 1
        ;;
        
    *)
        echo "Invalid input ^_^ "
        exit 1
        ;;
esac

echo "========== update =========="
apt update
apt upgrade -y

echo "========== install basic tools =========="
apt install -y linux-tools-common linux-tools-generic linux-tools-`uname -r`
apt install -y git wget curl gcc gdb clang vim python3 python3-pip tmux zsh tree cloc htop \
    scons fzf silversearcher-ag

apt install -y libcgroup-dev build-essential libnuma-dev

pip3 install meson ninja

apt install -y libcgroup-dev build-essential libnuma-dev meson

pip3 install ninja

echo "========== change bash to zsh =========="
chsh -s /bin/zsh

# modify /etc/hosts
echo "========== modify /etc/hosts to access github =========="
echo "\n# the following lines append for access github" >> $host_file
echo "199.232.68.133  raw.githubusercontent.com" >> $host_file
echo "199.232.68.133  raw.github.com" >> $host_file
echo "140.82.114.3    github.com" >> $host_file
echo "199.232.69.194  github.global.ssl.fastly.net" >> $host_file

# install oh-my-zsh
echo "========== install oh-my-zsh =========="
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# install vim config
echo "========== install vim plugins =========="
cd ~
mkdir -p .vim/autoload
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

echo "========== ALL done, enjoy yourself ==========\n"
