# TarSelected

Plugin for [fman.io](https://fman.io) to build a tarball from files that have been selected in fman.

Install with [fman's built-in command for installing plugins](https://fman.io/docs/installing-plugins).

This Plugin is based of ZipSelected fman Plugin by raguay.

I created this fork before I saw the fman Tarball plugin. That's why I chose to fork ZipSelected instead of fixing Tarball.

## Usage

Select the files you want to add to your tarball and execute the "Tar selected" command.

In the filename prompt you can choose to:
    
- Use no file compression by just enter a name
- Use gzip file compression by extending your name with .tar.gz
- Use bzip2 file compression by extending your name with .tar.bz2
- Use lzma file compression by extending your name with .tar.xz
