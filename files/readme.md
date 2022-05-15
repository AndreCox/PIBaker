# Example

Files in this directory can be accessed by Ansible. These then can be used when creating your customized Raspberry Pi OS image.

### How to use in Ansible

```
- name: Copy files to the RPI
  copy:
    src: /files/
    dest: /home/pi/
```

```
- name: Copy file to the RPI
  copy:
    src: /files/readme.md
    dest: /home/pi/readme.md
```
