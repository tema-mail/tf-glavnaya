# Сборка прототипа: kit.css внутрь <style>, раскладка по адресам Pages
import pathlib, shutil
root = pathlib.Path(__file__).parent
kit = (pathlib.Path.home() / '.claude/skills/marketolog/prototip/kit.css').read_text()
out = root / 'site'
shutil.rmtree(out, ignore_errors=True)
for src, dst in [('glavnaya.html', 'index.html'), ('otzyvy.html', 'otzyvy/index.html')]:
    p = out / dst; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text((root / 'src' / src).read_text().replace('/*KIT*/', kit))
shutil.copy(root / 'src/vidzhety-glavnaya.json', out / 'vidzhety-glavnaya.json')
(out / 'robots.txt').write_text('User-agent: *\nDisallow: /\n')
print('ok', [str(x.relative_to(out)) for x in out.rglob('*') if x.is_file()])
