#!/usr/bin/bash

touch $PREFIX/bin/automux

echo "clear" >> $PREFIX/bin/automux
echo "python $PREFIX/share/AutoMux/automux.py" >> automux

chmod +x $PREFIX/bin/automux

echo -e "\033[44m The End of \033[0m"
