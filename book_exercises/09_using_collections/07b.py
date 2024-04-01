info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

split_info = info.split(':')
joined_info = '+'.join(split_info)
print(joined_info)


# OR

result = info.replace(':',  '+')
print(result)