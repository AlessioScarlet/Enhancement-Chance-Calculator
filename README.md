# Enhancement Chance Calculator
**Enhancement (or drop) Chance Calculator made in python for Black Desert Online, Warframe, Minecraft or any other videogame.**

![](https://i.imgur.com/Ln326pk.png)

The formula it uses is this one:
## **( 1 - [ (1-X ) ^ (n° of runs) ] ) * 100**

Where X = probability / 100

**For example:**

I want to bring my Blackstar TRI to TET with 161 FS **(8.72%)**, and we suppose I've already done 10 taps.

( 1 - [ (1-0.0872) ^ (10) ] ) * 100 = (1 - 0.40156) * 100 = 0,5984 * 100 = 59.84%

# How to install:

### **Python**:
You will only need Python >=3.6

### **Windows**:
**Download the latest build [here](https://github.com/AlessioScarlet/Enhancement-Chance-Calculator/raw/main/ECC.exe)**

I compiled it with [autopytoexe](https://pypi.org/project/auto-py-to-exe/).
It will take some time to load (about 5 seconds).

### **Warning!**

When you download the .exe, your browser might detect it as a virus. It usually happens with programs that have got too few downloads.

The [VirusTotal Scan](https://www.virustotal.com/gui/file/ccef9af3f9926ac2e4ab9313e2dcf45bf5897a909b05883a4a184765f4bb557a/detection) shows that it's not harmful, at best it gets detected as a "Heuristic threat".

In any case, remember that you can always use the Python file, as it is opensource and you can just look at it.
