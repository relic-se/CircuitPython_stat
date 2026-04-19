# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2026 Cooper Dalrymple
#
# SPDX-License-Identifier: Unlicense

import stat

path = "/lib"
st = stat.stat(path)
print(stat.S_ISDIR(st.st_mode), stat.filemode(st.st_mode))
