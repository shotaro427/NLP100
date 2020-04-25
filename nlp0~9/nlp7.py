def create_template_text(x, y, z):
    return '%s時の%sは%s' % (x, y, z)

print(create_template_text('12', '気温', '22.4'))