# LinuxServerStudy

## Shell Use

### alias
create short order **in this shell window**
`alias ll="ls -la"`

To create permanent alias:
- enter `~/.bashrc`
- add alias order at last line
- to apply in current shell, `source ~/.bashrc`

### Pipe and Redirection

### shell file

File that can save shell script orders.

```shelltest.sh
#!/bin/bash    # what shell?

echo "this is shell test!"
```

how to run:
`sh shelltest.sh`
`bash shelltest.sh`

## How to use VIM

**Setting VIM**
- Save at `vim ~/.vimrc`
- ```~/.vimrc
  syntax on
  set tabstop=4
  set shiftwidth=4
  set smartindent    # auto indent
  set cindent
  ```

**Short cuts:**
- w: Save Changes
- q: Quit
- i: Insert Mode
- !: Dismiss (ex: !q)
- yny: Copy n lines
- pp: Paste
- dnd: Delete (and copy) n lines

## How to Connect Remote Server

### 1. Port Forwarding

1. Open gongyoogi settings.(type ip address)
2. Enter "Port Forwarding".
3. Add new rule.
4. Internal IP Address: Device IP
5. External Port -> Internal Port

### 2. SSH Connect

SSH(Secure Shell): Protocol that can control remote computer securely.

Powershell order: `ssh -p [Port] [login ID]@[gongyoogi ip]`

Putty: IP address, Port
