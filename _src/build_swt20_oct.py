# SWT論文20万 商品LP10月修正 初校ビルド
# 土台：公開中 science-web.tokyo/ronbun/（佐々木様共有の swt2026_toukou20_ver1.0 と創業日1行だけ異なる）
# 使い方：python3 -I build_swt20_oct.py <土台HTML> <出力HTML>
import sys

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf8').read()

def rep(old, new, count):
    global s
    n = s.count(old)
    if n != count:
        raise SystemExit(f'置換件数が違う（期待{count}・実際{n}）: {old[:80]!r}')
    s = s.replace(old, new)

BT_OLD = '<!-- BUILD_TAG: swt2026_toukou20_ver1.0 / 2026-09-16 -->'
BT_NEW = '<!-- BUILD_TAG: swt2026_toukou20_oct_ver1.0 / 2026-10-22 -->'
rep(BT_OLD, BT_NEW, 1)

# ---- 画像変更＋追加でスライドショーに（現在の画像は使わない） ----
rep('''    <div class="media-slot" id="mediaSlot">
      <img src="https://science-web.tokyo/images/system_outline.png" alt="開発イメージ">
      <!--<img src="https://science-web.tokyo/images/hero-02_sub05.jpg" alt="プログラマ">
      <img src="https://science-web.tokyo/images/hero-03_sub05.jpg" alt="ワークステーション">-->
    </div>''',
'''    <div class="media-slot" id="mediaSlot">
      <img src="images/system-outline.jpg" alt="論文投稿・査読システムの仕組み：投稿者・管理者・査読者がオンラインでつながり、論文の受付から判定まで管理できます" width="1821" height="864">
      <img src="images/slide-02.jpg" alt="データを確認しながら業務を進めるイメージ" width="7360" height="4140" loading="lazy">
      <img src="images/slide-03.jpg" alt="複数の画面で投稿状況を確認するイメージ" width="8192" height="4320" loading="lazy">
    </div>''', 1)

# ---- FAQ追加（「論文投稿のお悩みを、まとめて解決。」の下・緑ラインの位置） ----
FAQ = '''

    <div class="faq-box" id="qa">
      <h3 class="box-ttl faq-ttl">よくあるご質問</h3>
      <dl class="faq-list">
        <div class="faq-item">
          <dt>公開までどのくらいかかりますか？</dt>
          <dd>必要なデータの入稿完了から、3週間を目安に公開します。</dd>
        </div>
        <div class="faq-item">
          <dt>実際のシステムを見てから検討できますか？</dt>
          <dd>Zoomでデモ画面をご紹介できます。操作方法や運用イメージもご説明します。</dd>
        </div>
        <div class="faq-item">
          <dt>査読機能はありますか？</dt>
          <dd>20万円のスタンダードプランには査読機能は含まれていません。査読機能をご利用の場合は、30万円のプレミアムプランをご案内しています。</dd>
        </div>
      </dl>
    </div>'''
rep('''SSL対応で、安心してご利用いただけます。</span></p>
    </div>''', '''SSL対応で、安心してご利用いただけます。</span></p>
    </div>''' + FAQ, 1)

# ---- 電話追加（メール・Zoomボタンの横、3か所） ----
TEL = '\n      <a class="btn btn-tel" href="tel:05035387006">電話　050-3538-7006<br><small>（平日10時〜15時）</small></a>'
ZOOM_END = 'Zoom相談お申込み<small></a>'
rep(ZOOM_END, ZOOM_END + TEL, 3)
rep('<div class="btns two" style="margin-top:26px;">', '<div class="btns three" style="margin-top:26px;">', 3)

# ---- 「詳しくはこちら」を削除（追加できます：保守管理契約） ----
rep('<br><br><a class="bl-btn" href="https://science-web.tokyo/2026hosyu.pdf" target="_blank" rel="noopener">詳しくはこちら</a>', '', 1)

# ---- 会計書類ボタン（2か所）：発注書に「ダウンロード」、最適見積書の説明を変更 ----
rep('<button class="btn-doc b3" data-open="m-order">発注書<br><small>入力してそのまま送信</small></button>',
    '<button class="btn-doc b3" data-open="m-order">発注書<br>ダウンロード<br><small>入力してそのまま送信</small></button>', 2)
rep('<small>カスタマイズ可能</small>', '<small>基本見積にカスタマイズを追加できます</small>', 2)

# ---- 料金プラン一覧：プラン名をリンクに ----
rep('<div class="tc-ttl">5万円｜ベーシックプラン　<a href="https://science-web.tokyo/ronbun.trial/" target="_blank" rel="noopener">→</a></div>',
    '<div class="tc-ttl"><a class="plan-link" href="https://science-web.tokyo/ronbun.trial/" target="_blank" rel="noopener">5万円｜ベーシックプラン<span class="pl-arrow" aria-hidden="true">→</span></a></div>', 1)
rep('<div class="tc-ttl">20万円｜スタンダードプラン　<a href="https://science-web.tokyo/ronbun/" target="_blank" rel="noopener">→</a></div>',
    '<div class="tc-ttl"><a class="plan-link" href="https://science-web.tokyo/ronbun/" target="_blank" rel="noopener">20万円｜スタンダードプラン<span class="pl-arrow" aria-hidden="true">→</span></a></div>', 1)

# ---- 枠の区画を削除（他のシステムとの組み合わせも可能です。） ----
FREEBOX = '''    <div class="freebox">
      <h3 class="box-ttl">他のシステムとの組み合わせも可能です。</h3>
      <ul class="free">
        <li><span style="font-size: 1.5rem;">紀要管理　30万円</span><b><a href="https://science-web.tokyo/bulletin/" target="_blank" rel="noopener">→</a></b></li>
        <li><span style="font-size: 1.5rem;">学会事務　20万円</span><b><a href="https://science-web.tokyo/jimu-system/#top" target="_blank" rel="noopener">→</a></b></li>
        <li><span style="font-size: 1.5rem;">役員選挙　20万円</span><b><a href="https://science-web.tokyo/senkyo/" target="_blank" rel="noopener">→</a></b></li>
        <li><span style="font-size: 1.5rem;">動画配信　32万円</span><b><a href="https://medical-streaming.tokyo/#" target="_blank" rel="noopener">→</a></b></li>
      </ul>
    </div>
''' + '    ' + '\n'
rep(FREEBOX, '', 1)

# ---- 取引実績：学会・国立研究開発法人を書き換え ----
rep('''            <li>応用物理学会</li>
            <li>国際会計研究学会</li>
            <li>静電気学会</li>
            <li>畜産学会</li>
            <li>中部森林学会</li>
            <li>日本分光学会、ほか</li>''',
'''            <li>日本国際保健医療学会</li>
            <li>日本TDM学会</li>
            <li>日本口腔腫瘍学会</li>
            <li>日本抗体学会</li>
            <li>日本地震学会</li>
            <li>土木学会、ほか</li>''', 1)
rep('''            <li>産業技術総合研究所</li>
            <li>物質・材料研究機構</li>
            <li>JAXA、ほか</li>''',
'''            <li>理化学研究所</li>
            <li>国立精神・神経医療研究センター</li>
            <li>国立がん研究センター東病院臨床開発センター</li>
            <li>宇宙航空研究開発機構（JAXA）</li>
            <li>産業技術総合研究所</li>
            <li>国立感染症研究所、ほか</li>''', 1)

# ---- FAQ の構造化データ ----
FAQ_LD = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "公開までどのくらいかかりますか？",
     "acceptedAnswer": {"@type": "Answer", "text": "必要なデータの入稿完了から、3週間を目安に公開します。"}},
    {"@type": "Question", "name": "実際のシステムを見てから検討できますか？",
     "acceptedAnswer": {"@type": "Answer", "text": "Zoomでデモ画面をご紹介できます。操作方法や運用イメージもご説明します。"}},
    {"@type": "Question", "name": "査読機能はありますか？",
     "acceptedAnswer": {"@type": "Answer", "text": "20万円のスタンダードプランには査読機能は含まれていません。査読機能をご利用の場合は、30万円のプレミアムプランをご案内しています。"}}
  ]
}
</script>
'''

# ---- 追加CSS（最後の style の末尾） ----
CSS = '''
/* ===== 10月修正：ここから ===== */
/* 文字サイズ2倍（トップ） */
.hero h1{font-size:clamp(38px,10vw,88px);}
.hero h1 .sub{font-size:clamp(17px,5vw,38px);}
.hero-card .hc-left .n{font-size:24px;}
.hero-card .hc-left .p-tax{font-size:24px;}
.hero-card .hc-right .n{font-size:22px;}
.hero-card .hc-right .p-tax{font-size:22px;}
/* 「3週間」を左の「20万円」と同じ大きさに */
.hero-card .hc-right .p-num{font-size:92px;}
.hero-card .hc-right .p-unit{font-size:38px;}
@media (max-width:700px){
  .hero-card .hc-left .n,.hero-card .hc-left .p-tax{font-size:20px;}
  .hero-card .hc-right .n,.hero-card .hc-right .p-tax{font-size:18px;}
  .hero-card .hc-left .p-num,.hero-card .hc-right .p-num{font-size:72px;}
  .hero-card .hc-left .p-unit,.hero-card .hc-right .p-unit{font-size:30px;}
}
/* スライドショー：画像の比率（16:9）に合わせる */
.media-slot,.media-slot:has(img){aspect-ratio:16/9;}
@media (max-width:760px){ .media-slot{aspect-ratio:16/9;} }
/* よくあるご質問 */
.faq-box{margin-top:28px;background:#fff;border:1px solid var(--rule);border-radius:6px;padding:26px 28px;}
.faq-list{margin:0;}
.faq-item{padding:14px 0;border-top:1px solid var(--rule);}
.faq-item:first-child{border-top:0;padding-top:4px;}
.faq-item dt{font-size:16px;font-weight:800;color:var(--navy);line-height:1.6;}
.faq-item dt::before{content:"Q.";margin-right:8px;}
.faq-item dd{margin:6px 0 0;font-size:15px;color:var(--ink);line-height:1.8;}
.faq-item dd::before{content:"A.";margin-right:8px;font-weight:800;}
@media (max-width:560px){ .faq-box{padding:20px 18px;} }
/* 電話ボタン（3つ並び） */
.btns.three{grid-template-columns:repeat(3,1fr);}
@media (max-width:820px){ .btns.three{grid-template-columns:1fr;} }
.btn-tel{background:#fff;color:var(--navy);border:2px solid var(--navy);}
/* 料金プラン一覧：プラン名をリンクに */
.tc-ttl .plan-link{color:var(--navy);text-decoration:underline;text-underline-offset:4px;}
.tc-ttl .plan-link:hover{opacity:.8;}
.tc-ttl .pl-arrow{margin-left:10px;text-decoration:none;display:inline-block;}
/* ===== 10月修正：ここまで ===== */
'''
rep('''.lead{font-size:15px;line-height:1.9;margin:0}
.sec-ttl{margin:0 0 12px}
</style>
</head>''', '''.lead{font-size:15px;line-height:1.9;margin:0}
.sec-ttl{margin:0 0 12px}''' + CSS + '''</style>
''' + FAQ_LD + '''</head>''', 1)

open(dst, 'w', encoding='utf8').write(s)
print('ok', len(s))
