import asyncio, sys
from playwright.async_api import async_playwright
URL = sys.argv[1]; OUT = sys.argv[2]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        errs = []
        for w in (320, 375, 414, 768, 1024, 1440):
            pg = await b.new_page(viewport={'width': w, 'height': 900})
            pg.on('pageerror', lambda e: errs.append(str(e)))
            await pg.goto(URL, wait_until='load')
            await pg.wait_for_timeout(800)
            sw = await pg.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth')
            info = await pg.evaluate('''()=>{const q=s=>document.querySelector(s);const r=e=>e?Math.round(e.getBoundingClientRect().top+scrollY):null;
              return {h1:getComputedStyle(q('.hero h1 .kw')).fontSize, sub:getComputedStyle(q('.hero h1 .sub')).fontSize,
                ln:getComputedStyle(q('.hc-left .n')).fontSize, rnum:getComputedStyle(q('.hc-right .p-num')).fontSize, lnum:getComputedStyle(q('.hc-left .p-num')).fontSize,
                faqTop:r(q('#qa')), tel:document.querySelectorAll('.btn-tel').length, imgs:[...document.querySelectorAll('#mediaSlot img')].map(i=>i.naturalWidth)}}''')
            print(w, 'hscroll', sw, info)
            if w in (375, 1440):
                await pg.evaluate('document.querySelectorAll("img[loading=lazy]").forEach(i=>i.loading="eager")')
                await pg.wait_for_timeout(1500)
                await pg.screenshot(path=f'{OUT}/full_{w}.png', full_page=True)
            if w == 1440:
                for m in ('m-basic','m-ref','m-order'):
                    await pg.click(f'.doc-btns button[data-open="{m}"]')
                    await pg.wait_for_timeout(300)
                    vis = await pg.evaluate(f'(()=>{{const e=document.getElementById("{m}");return !!e && getComputedStyle(e).display!=="none"}})()')
                    print('modal', m, vis)
                    await pg.keyboard.press('Escape'); await pg.wait_for_timeout(200)
                    await pg.goto(URL, wait_until='load')
                # slideshow switch
                a = await pg.evaluate('[...document.querySelectorAll("#mediaSlot img")].findIndex(i=>i.classList.contains("on"))')
                await pg.wait_for_timeout(5300)
                c = await pg.evaluate('[...document.querySelectorAll("#mediaSlot img")].findIndex(i=>i.classList.contains("on"))')
                print('slide on index', a, '->', c)
            await pg.close()
        print('pageerrors', errs)
        await b.close()
asyncio.run(main())
