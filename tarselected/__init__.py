from fman import DirectoryPaneCommand, show_alert, show_prompt
from fman.url import as_human_readable
import os
import tarfile

SUPPORTED_EXTENSIONS=["xz","gz","bz2"]

class TarSelected(DirectoryPaneCommand):
    def __call__(self):
        selected_files = self.pane.get_selected_files()
        if len(selected_files) >= 1 or (len(selected_files) == 0 and self.get_chosen_files()):
            if len(selected_files) == 0 and self.get_chosen_files():
                selected_files.append(self.get_chosen_files()[0])
            dirPath = os.path.dirname(as_human_readable(selected_files[0]))
            infoText = 'Please enter a name for your tar file.\nYour tarball will be compressed according to the file etension.\nThe following extensions for file compression are supported:\n\n'
            for ext in SUPPORTED_EXTENSIONS:
                infoText += "*." + ext + "\n"
            infoText += "\nExample: test.tar.gz"
            infoText += "\n\nIf no compression is desired you can just enter the name without file extension\n"
            tarName, ok = show_prompt(infoText)
            if not tarName or not ok:
                show_alert("Creating tarball canceled")
                return
            tarPath = os.path.join(dirPath, tarName)
            extension = os.path.splitext(tarName)[1][1:]
            if extension not in SUPPORTED_EXTENSIONS:
                tarPath += ".tar"
                extension = ""
            numitems = 0
            with tarfile.open(tarPath,'w:' + extension) as target:
                for file in selected_files:
                    file = as_human_readable(file)
                    relative = os.path.relpath(file,dirPath)
                    target.add(file,arcname=relative)
                    numitems += 1
            show_alert(str(numitems) + " items added to " + tarName)
        else:
            show_alert("No files or directories selected")
        

