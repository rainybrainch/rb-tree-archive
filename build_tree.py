"""RB-Tree Archive — 縦型樹形図ジェネレーター"""

# ── Subject definitions ──────────────────────────────────────────
SUBJECTS = {
  "economics": {
    "title": "RB-Tree Economics — 経済の樹",
    "nav":   "Economics",
    "icon":  "🌳",
    "stream": "https://rainybrainch.github.io/live/streams/economy.html",
    "archive_key": "rbt_data_v1",
    "seed_prefix": "E",
    "db_var": "SEED_DB",
    "seeds_js": "seeds/seeds-data.js",
    "acc": "#c9a84c", "acc2": "#8a6f2a",
    "bg": "#050a05", "bg2": "#0a120a", "text": "#d4e8d0",
    "line_color": "rgba(201,168,76,",
    "level_descs": {"ROOT":"経済の根","TRUNK":"動かす幹","BRANCH":"現実の枝","CROWN":"世界の樹冠","FOREST":"経済史の森"},
    # (num, name, level, sub, parent_num or None)
    "seeds": [
      (1,"お金","ROOT","通貨・信用・円。なぜ紙切れに価値があるのか。",None),
      (2,"銀行","ROOT","預金・融資・信用創造。お金を社会に流す装置。",None),
      (3,"物価","ROOT","インフレ・デフレ・需要と供給。価格水準の動き。",None),
      (4,"景気","ROOT","好景気・不景気・景気循環。経済全体の調子。",None),
      (5,"GDP","ROOT","国内総生産・経済成長。国の経済規模の指標。",None),
      (6,"金利","TRUNK","利上げ・利下げ・政策金利。お金を借りるレンタル料。",1),
      (7,"中央銀行","TRUNK","日本銀行・FRB・金融政策。物価を安定させる機関。",2),
      (8,"為替","TRUNK","円高・円安・ドル円。通貨同士の交換レート。",1),
      (9,"国債","TRUNK","政府の借金・利回り・長期金利。",2),
      (10,"雇用","TRUNK","失業率・賃金・求人倍率。景気・消費をつなぐ指標。",4),
      (11,"エネルギー","BRANCH","原油・天然ガス・資源価格。物価と企業コストに影響。",8),
      (12,"貿易","BRANCH","輸出・輸入・貿易収支。世界経済とつながる仕組み。",8),
      (13,"人口","BRANCH","少子高齢化・労働人口。経済成長と社会保障の基盤。",10),
      (14,"不動産","BRANCH","住宅価格・金利・景気との関係。資産市場の代表。",6),
      (15,"AI・技術","BRANCH","生産性・イノベーション・雇用代替。技術変化と経済。",5),
      (16,"米国経済","CROWN","FRB・ドル・米国株。世界経済と金融市場の中心。",9),
      (17,"中国経済","CROWN","製造・貿易・不動産。世界に大きな影響を持つ経済大国。",12),
      (18,"日本経済","CROWN","低成長・少子高齢化・円安・財政。日本固有の課題。",7),
      (19,"EU経済","CROWN","ユーロ・ECB。複数国の共通通貨圏。",11),
      (20,"新興国","CROWN","高成長・通貨リスク・人口増加。",13),
      (21,"世界恐慌","FOREST","1929年・株価暴落。金融危機が実体経済へ波及。",16),
      (22,"オイルショック","FOREST","原油・スタグフレーション・供給ショック。",19),
      (23,"バブル経済","FOREST","不動産・株価・信用膨張。資産価格の過剰膨張。",18),
      (24,"ITバブル","FOREST","インターネット・NASDAQ・期待過剰。",15),
      (25,"リーマン\nショック","FOREST","サブプライム・証券化・金融危機。",16),
      (26,"コロナ\nショック","FOREST","ロックダウン・給付金・インフレ。",20),
    ]
  },
  "politics": {
    "title": "RB-Tree Politics — 政治の樹",
    "nav":   "Politics",
    "icon":  "🏛",
    "stream": "https://rainybrainch.github.io/live/streams/politics.html",
    "archive_key": "rbt_politics_v1",
    "seed_prefix": "P",
    "db_var": "POLITICS_DB",
    "seeds_js": "seeds/politics-data.js",
    "acc": "#6bb6ff", "acc2": "#2a5a8a",
    "bg": "#040810", "bg2": "#080c18", "text": "#c8dff0",
    "line_color": "rgba(107,182,255,",
    "level_descs": {"ROOT":"民主主義の根","TRUNK":"国家の幹","BRANCH":"現代社会の枝","CROWN":"世界の政治","FOREST":"政治史の森"},
    "seeds": [
      (1,"選挙","ROOT","投票・選挙制度・民主主義の根本。",None),
      (2,"政党","ROOT","与党・野党・政策綱領。政治理念でつながる組織。",None),
      (3,"国会","ROOT","衆議院・参議院・法律制定。国権の最高機関。",None),
      (4,"内閣","ROOT","首相・閣議・行政権。政策を実行する最高機関。",None),
      (5,"憲法","ROOT","三大原則・立憲主義・最高法規。権力を縛るルール。",None),
      (6,"予算・財政","TRUNK","国債・社会保障費・財政再建。政策の優先順位を示す設計図。",4),
      (7,"外交","TRUNK","日米同盟・ODA・国際交渉。国益を守る対外活動。",5),
      (8,"安全保障","TRUNK","専守防衛・集団的自衛権・防衛費。国を守る仕組み。",5),
      (9,"地方自治","TRUNK","都道府県・市区町村・地方交付税。地域の自主運営。",3),
      (10,"行政・官僚","TRUNK","官僚制・縦割り行政・政治主導。政策を実行する機構。",4),
      (11,"メディア","BRANCH","議題設定・SNS・フェイクニュース。情報と民主主義の関係。",1),
      (12,"世論・民意","BRANCH","内閣支持率・ポピュリズム・利益集団。民意の形成と政治。",2),
      (13,"市民社会","BRANCH","NGO・NPO・ロビイング。国家でも市場でもない活動領域。",9),
      (14,"国際機関","BRANCH","国連・IMF・WTO。国境を越えた協調の仕組み。",7),
      (15,"条約・国際法","BRANCH","条約・慣習法・主権。国家間のルールと強制力。",8),
      (16,"日本の政治","CROWN","55年体制・政権交代・政治改革。日本固有の課題。",6),
      (17,"米国の政治","CROWN","大統領制・二大政党・選挙人制度。世界最大の民主主義。",14),
      (18,"中国の政治","CROWN","一党支配・習近平・全国人民代表大会。権威主義の現代型。",14),
      (19,"EU・欧州","CROWN","欧州統合・Brexit・右翼ポピュリズム。超国家機関の実験。",15),
      (20,"民主主義の\n後退","CROWN","選挙的権威主義・司法の独立・民主主義崩壊。現代の脅威。",12),
      (21,"戦後日本史","FOREST","55年体制・安保闘争・政権交代。日本現代史の核心。",16),
      (22,"冷戦","FOREST","米ソ対立・核抑止・代理戦争。二極構造が生んだ時代。",17),
      (23,"アラブの春","FOREST","中東民主化・SNS革命・内戦。独裁打倒後の現実。",18),
      (24,"ポピュリズム","FOREST","格差・エリート批判・トランプ。民主主義の変容。",20),
      (25,"核・軍縮","FOREST","NPT・核抑止・核禁止条約。人類最大の安全保障課題。",19),
      (26,"気候変動と\n政治","FOREST","パリ協定・カーボンニュートラル・グリーン政治。",13),
    ]
  },
  "investment": {
    "title": "RB-Tree Investment — 投資の樹",
    "nav":   "Investment",
    "icon":  "📈",
    "stream": "https://rainybrainch.github.io/live/streams/investment.html",
    "archive_key": "rbt_invest_v1",
    "seed_prefix": "I",
    "db_var": "INVESTMENT_DB",
    "seeds_js": "seeds/investment-data.js",
    "acc": "#57c87c", "acc2": "#1a5a30",
    "bg": "#040a06", "bg2": "#081208", "text": "#c8f0d8",
    "line_color": "rgba(87,200,124,",
    "level_descs": {"ROOT":"投資の根","TRUNK":"投資の幹","BRANCH":"現実の枝","CROWN":"高度な投資","FOREST":"投資の歴史"},
    "seeds": [
      (1,"株式","ROOT","株・配当・株主権。企業の所有権の一部を買う。",None),
      (2,"債券","ROOT","国債・社債・利回り。政府・企業への貸し付け。",None),
      (3,"投資信託","ROOT","ファンド・運用・分散。専門家に運用を任せる仕組み。",None),
      (4,"リスクと\nリターン","ROOT","期待収益・標準偏差・リスク許容度。投資の基本原理。",None),
      (5,"複利","ROOT","利息の利息・72の法則・時間の価値。投資最大の武器。",None),
      (6,"分散投資","TRUNK","卵を一つのかごに盛るな。相関係数・リスク低減。",4),
      (7,"アセット\nアロケーション","TRUNK","株・債券・不動産・現金の配分。リターンの9割を決める。",6),
      (8,"インデックス\n投資","TRUNK","S&P500・全世界株・低コスト。市場平均を買う戦略。",3),
      (9,"長期投資","TRUNK","バイアンドホールド・時間分散・市場の上下を乗り越える。",5),
      (10,"NISA・iDeCo","TRUNK","非課税・老後資産形成・年間投資枠。日本の税優遇制度。",9),
      (11,"テクニカル\n分析","BRANCH","チャート・移動平均・RSI。過去の価格から未来を読む試み。",1),
      (12,"ファンダメンタル\n分析","BRANCH","PER・PBR・ROE。企業の実力で株価を測る。",1),
      (13,"ETF","BRANCH","上場投資信託・低コスト・流動性。株のように取引できる投信。",8),
      (14,"不動産・REIT","BRANCH","REIT・家賃収入・レバレッジ。現物以外の不動産投資。",7),
      (15,"外国株・為替","BRANCH","米国株・新興国・為替ヘッジ。国際分散と通貨リスク。",10),
      (16,"米国株・\nS&P500","CROWN","S&P500・NYSE・NASDAQ。世界最大株式市場の特徴。",13),
      (17,"新興国投資","CROWN","BRICs・高成長・通貨リスク・政治リスク。",15),
      (18,"バリュー・\nグロース","CROWN","割安株・成長株・バフェット流。投資哲学の二大潮流。",12),
      (19,"ポートフォリオ\n理論","CROWN","効率的フロンティア・シャープレシオ・MPT。現代投資理論の基礎。",7),
      (20,"オルタナティブ\n投資","CROWN","ヘッジファンド・PE・コモディティ。伝統的資産以外への投資。",14),
      (21,"ブラック\nマンデー","FOREST","1987年暴落・プログラム売買・株価-22%。歴史的一日の教訓。",16),
      (22,"バブルと暴落","FOREST","投機・群衆心理・マナー則。繰り返される資産バブルのパターン。",18),
      (23,"リーマンと\n投資","FOREST","金融危機・暴落と回復・長期保有の威力。歴史最大の試練。",16),
      (24,"コロナと市場","FOREST","コロナ暴落・急回復・FRBの量的緩和。過去最速の回復劇。",17),
      (25,"FIRE運動","FOREST","経済的自立・早期引退・4%ルール。新しい人生設計の考え方。",10),
      (26,"インフレと\n投資","FOREST","インフレヘッジ・実物資産・株式の実質リターン。物価上昇への対策。",19),
    ]
  }
}

LEVEL_COLORS = {
  "ROOT":   ("#c9a84c", "rgba(201,168,76,"),
  "TRUNK":  ("#57c87c", "rgba(87,200,124,"),
  "BRANCH": ("#5aafcf", "rgba(90,175,207,"),
  "CROWN":  ("#b68cdf", "rgba(182,140,223,"),
  "FOREST": ("#e07878", "rgba(224,120,120,"),
}
LEVEL_ICONS = {"ROOT":"🌱","TRUNK":"🌿","BRANCH":"🍃","CROWN":"🌳","FOREST":"🌲"}

def jstr(s):
    return '"' + str(s).replace('\\','\\\\').replace('"','\\"') + '"'

def seeds_js_array(seeds):
    lines = []
    for num,name,level,sub,parent in seeds:
        p = "null" if parent is None else str(parent)
        lines.append(
            f"  {{num:{num},name:{jstr(name)},level:{jstr(level)},"
            f"sub:{jstr(sub)},parent:{p},ready:true}}"
        )
    return "[\n" + ",\n".join(lines) + "\n]"

def make_html(slug, subj):
    tab_parts = []
    for s2, d2 in SUBJECTS.items():
        cls = ' class="tab-active"' if s2 == slug else ''
        tab_parts.append(f'<a href="{s2}.html"{cls}>{d2["icon"]} {d2["nav"]}</a>')
    tabs_html = "\n    ".join(tab_parts)
    seeds_arr = seeds_js_array(subj["seeds"])
    ldescs_js = "{" + ",".join(f'{jstr(k)}:{jstr(v)}' for k,v in subj["level_descs"].items()) + "}"
    lcolors_js = "{" + ",".join(
        f'{jstr(lv)}:{{c:{jstr(c)},r:{jstr(r)}}}'
        for lv,(c,r) in LEVEL_COLORS.items()
    ) + "}"
    licons_js  = "{" + ",".join(f'{jstr(k)}:{jstr(v)}' for k,v in LEVEL_ICONS.items()) + "}"

    acc = subj["acc"]
    bg  = subj["bg"]
    bg2 = subj["bg2"]
    txt = subj["text"]
    lc  = subj["line_color"]

    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{subj["title"]}</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@400;700&family=Noto+Sans+JP:wght@400;700;900&display=swap" rel="stylesheet">
<style>
:root{{
  --bg:{bg};--bg2:{bg2};--acc:{acc};--acc2:{subj["acc2"]};
  --text:{txt};--muted:{lc}.5);--faint:{lc}.25);
  --font:"Noto Sans JP",sans-serif;--serif:"Noto Serif JP",serif;
  color-scheme:dark;
}}
*{{box-sizing:border-box;margin:0;padding:0;}}
html,body{{height:100%;background:var(--bg);color:var(--text);font-family:var(--font);overflow:hidden;display:flex;flex-direction:column;}}
/* ── HEADER ── */
.hd{{
  flex-shrink:0;height:52px;display:flex;align-items:center;gap:10px;padding:0 18px;
  background:rgba(4,8,4,.97);backdrop-filter:blur(18px);
  border-bottom:1px solid rgba(255,255,255,.07);z-index:30;
}}
.logo{{display:flex;align-items:center;gap:8px;font-family:var(--serif);font-size:15px;font-weight:700;}}
.tabs{{display:flex;gap:3px;margin-left:6px;}}
.tabs a{{padding:5px 12px;border-radius:7px;font-size:11px;font-weight:900;
  color:rgba(255,255,255,.4);text-decoration:none;transition:all .15s;border:1px solid transparent;}}
.tabs a:hover{{color:var(--text);background:rgba(255,255,255,.06);}}
.tabs a.tab-active{{color:var(--acc);background:{lc}.1);border-color:{lc}.3);}}
.hd-right{{margin-left:auto;display:flex;gap:7px;}}
.btn{{padding:5px 13px;border-radius:7px;border:1px solid rgba(255,255,255,.1);
  background:rgba(255,255,255,.04);font-size:11px;font-weight:900;
  text-decoration:none;color:rgba(255,255,255,.45);transition:all .15s;}}
.btn:hover{{color:var(--text);background:rgba(255,255,255,.09);}}
.btn-acc{{border-color:{lc}.3);background:{lc}.09);color:var(--acc);}}
.btn-acc:hover{{background:{lc}.18);}}
/* ── SUBHEADER ── */
.sub{{
  flex-shrink:0;height:38px;display:flex;align-items:center;gap:14px;padding:0 18px;
  border-bottom:1px solid rgba(255,255,255,.05);background:rgba(4,8,4,.88);
}}
.pb-wrap{{display:flex;align-items:center;gap:8px;flex:1;max-width:380px;margin-left:4px;}}
.pb-track{{flex:1;height:5px;border-radius:999px;background:rgba(255,255,255,.08);overflow:hidden;}}
.pb-fill{{height:100%;border-radius:999px;background:linear-gradient(90deg,var(--acc2),var(--acc));transition:width .6s;}}
.pb-lbl{{font-size:10px;font-weight:900;color:var(--muted);white-space:nowrap;}}
.chips{{display:flex;gap:5px;margin-left:auto;}}
.chip{{font-size:10px;font-weight:900;padding:3px 10px;border-radius:999px;
  border:1px solid rgba(255,255,255,.1);color:rgba(255,255,255,.38);}}
.chip.d{{border-color:{lc}.38);color:var(--acc);background:{lc}.08);}}
.chip.w{{border-color:rgba(87,200,124,.32);color:#57c87c;background:rgba(87,200,124,.07);}}
/* ── BODY ── */
.body{{flex:1;display:flex;overflow:hidden;}}
/* ── TREE ── */
.tree{{
  flex:1;overflow:auto;cursor:grab;position:relative;
  scrollbar-width:thin;scrollbar-color:{lc}.15) transparent;
  background:
    radial-gradient(ellipse at 50% 0%,{lc}.08),transparent 50%),
    radial-gradient(ellipse at 20% 100%,{lc}.04),transparent 40%),
    var(--bg);
}}
.tree::before{{
  content:"";position:absolute;inset:0;pointer-events:none;
  background:
    linear-gradient({lc}.015) 1px,transparent 1px) 0 0/64px 64px,
    linear-gradient(90deg,{lc}.015) 1px,transparent 1px) 0 0/64px 64px;
}}
.tree:active{{cursor:grabbing;}}
/* ── PANEL ── */
.panel{{
  width:0;overflow:hidden;flex-shrink:0;
  background:linear-gradient(180deg,rgba(255,255,255,.04),rgba(255,255,255,.015)),{bg2};
  border-left:1px solid rgba(255,255,255,.07);
  display:flex;flex-direction:column;
  transition:width .26s cubic-bezier(.4,0,.2,1);
}}
.panel.open{{width:340px;}}
.ph{{flex-shrink:0;padding:14px 16px;border-bottom:1px solid rgba(255,255,255,.07);
  background:rgba(255,255,255,.025);display:flex;align-items:flex-start;gap:10px;}}
.ph-badge{{font-size:9px;font-weight:900;letter-spacing:.12em;padding:3px 9px;border-radius:999px;
  border:1px solid var(--acc);color:var(--acc);background:{lc}.08);
  white-space:nowrap;flex-shrink:0;margin-top:2px;}}
.ph-title{{font-family:var(--serif);font-size:18px;font-weight:700;flex:1;line-height:1.2;}}
.ph-close{{background:0;border:1px solid rgba(255,255,255,.1);border-radius:6px;
  font-size:12px;color:rgba(255,255,255,.45);cursor:pointer;padding:3px 9px;transition:all .15s;flex-shrink:0;}}
.ph-close:hover{{color:var(--text);}}
.pb{{flex:1;overflow-y:auto;padding:14px 16px;display:flex;flex-direction:column;gap:13px;
  scrollbar-width:thin;}}
.tagline{{font-family:var(--serif);font-size:13px;line-height:1.7;
  border-left:3px solid var(--acc);padding:7px 12px;
  background:{lc}.04);border-radius:0 8px 8px 0;}}
.sec{{display:flex;flex-direction:column;gap:5px;}}
.sec-lbl{{font-size:9px;font-weight:900;letter-spacing:.14em;text-transform:uppercase;
  color:{lc}.5);padding-bottom:5px;border-bottom:1px solid rgba(255,255,255,.06);}}
.rq{{font-size:11px;color:var(--muted);padding:5px 8px;background:rgba(255,255,255,.025);
  border-radius:6px;line-height:1.5;border-left:2px solid {lc}.2);}}
.sp{{font-size:11px;color:var(--muted);padding:6px 10px;
  background:rgba(255,255,255,.02);border-radius:7px;
  border:1px solid rgba(255,255,255,.06);line-height:1.4;
  cursor:pointer;transition:all .15s;text-align:left;width:100%;
  display:flex;align-items:flex-start;gap:6px;}}
.sp:hover{{background:rgba(224,120,120,.07);border-color:rgba(224,120,120,.25);color:var(--text);}}
.sp::before{{content:"⏸";font-size:10px;flex-shrink:0;margin-top:1px;}}
.kws{{display:flex;flex-wrap:wrap;gap:5px;}}
.kw{{font-size:10px;font-weight:700;padding:2px 8px;border-radius:999px;
  border:1px solid {lc}.22);background:{lc}.07);color:var(--acc);}}
.acts{{display:flex;gap:7px;}}
.act{{flex:1;padding:9px;border-radius:8px;font-size:11px;font-weight:900;
  cursor:pointer;transition:all .15s;border:1px solid rgba(255,255,255,.1);
  background:rgba(255,255,255,.04);color:rgba(255,255,255,.45);}}
.act.done{{border-color:{lc}.42);background:{lc}.12);color:var(--acc);}}
.act.wip{{border-color:rgba(87,200,124,.35);background:rgba(87,200,124,.1);color:#57c87c;}}
.act:hover{{filter:brightness(1.15);}}
.p-link{{display:flex;align-items:center;justify-content:center;gap:6px;
  padding:9px;border-radius:8px;text-decoration:none;font-size:11px;font-weight:900;
  border:1px solid {lc}.3);background:{lc}.07);color:var(--acc);transition:background .15s;}}
.p-link:hover{{background:{lc}.18);}}
/* ── TOAST ── */
.toast{{position:fixed;bottom:18px;left:50%;transform:translateX(-50%);
  padding:7px 18px;border-radius:999px;background:rgba(4,8,4,.95);
  border:1px solid {lc}.35);color:var(--acc);font-size:12px;font-weight:900;
  pointer-events:none;z-index:100;opacity:0;transition:opacity .22s;white-space:nowrap;}}
.toast.on{{opacity:1;}}
/* ── LEGEND ── */
.legend{{position:absolute;bottom:14px;left:14px;z-index:8;
  padding:9px 13px;border-radius:10px;
  background:rgba(4,8,4,.9);backdrop-filter:blur(14px);
  border:1px solid rgba(255,255,255,.07);
  display:flex;flex-direction:column;gap:4px;}}
.lg-title{{font-size:8px;font-weight:900;letter-spacing:.14em;color:rgba(255,255,255,.25);margin-bottom:2px;text-transform:uppercase;}}
.lg-row{{display:flex;align-items:center;gap:7px;font-size:10px;font-weight:900;color:var(--muted);}}
.lg-dot{{width:10px;height:10px;border-radius:3px;flex-shrink:0;}}
</style>
</head>
<body>
<header class="hd">
  <div class="logo"><span style="font-size:22px;">{subj["icon"]}</span>RB-Tree</div>
  <nav class="tabs">
    {tabs_html}
  </nav>
  <div class="hd-right">
    <a class="btn btn-acc" href="{subj["stream"]}" target="_blank">📡 配信</a>
    <a class="btn" href="index.html">Archive 一覧</a>
  </div>
</header>
<div class="sub">
  <span style="font-size:11px;font-weight:900;color:var(--muted);letter-spacing:.08em;">{subj["nav"]}</span>
  <div class="pb-wrap">
    <div class="pb-track"><div class="pb-fill" id="pbFill" style="width:0%"></div></div>
    <span class="pb-lbl" id="pbLbl">0 / 26</span>
  </div>
  <div class="chips">
    <span class="chip d" id="cDone">完了 0</span>
    <span class="chip w" id="cWip">学習中 0</span>
    <span class="chip"   id="cNone">未着手 26</span>
  </div>
</div>
<div class="body">
  <div class="tree" id="tree">
    <svg id="svg" xmlns="http://www.w3.org/2000/svg"></svg>
    <div class="legend">
      <div class="lg-title">凡例</div>
      <div class="lg-row"><span class="lg-dot" style="background:{lc}.1);border:1.5px solid {lc}.32);"></span>未着手</div>
      <div class="lg-row"><span class="lg-dot" style="background:{lc}.22);border:1.5px solid {lc}.75);"></span>完了 ✓</div>
      <div class="lg-row"><span class="lg-dot" style="background:rgba(87,200,124,.15);border:1.5px solid rgba(87,200,124,.65);"></span>学習中</div>
    </div>
  </div>
  <aside class="panel" id="panel">
    <div class="ph">
      <div style="flex:1;min-width:0;">
        <div class="ph-badge" id="pLevel">ROOT</div>
        <div class="ph-title" id="pTitle" style="margin-top:6px;">—</div>
      </div>
      <button class="ph-close" onclick="closePanel()">✕</button>
    </div>
    <div class="pb" id="pBody"></div>
  </aside>
</div>
<div class="toast" id="toast"></div>

<script src="{subj["seeds_js"]}"></script>
<script src="seeds/seeds-data.js" onerror="void 0"></script>
<script>
(()=>{{
"use strict";
const AK={jstr(subj["archive_key"])};
const STREAM={jstr(subj["stream"])};
const PFX={jstr(subj["seed_prefix"])};
const DBVAR={jstr(subj["db_var"])};
const LDESCS={ldescs_js};
const LC={lcolors_js};
const LI={licons_js};
const LEVELS=["ROOT","TRUNK","BRANCH","CROWN","FOREST"];
const SEEDS={seeds_arr};

// ── Status ──
const statusMap={{}};
function loadStatus(){{
  try{{
    (JSON.parse(localStorage.getItem(AK)||"[]")).forEach(e=>{{
      SEEDS.forEach(s=>{{if(s.name.replace(/\\n/g,"")===e.keyword||s.name===e.keyword)
        statusMap[s.num]=(e.stage==="forest"||e.stage==="tree")?"done":"wip";
      }});
    }});
  }}catch{{}}
}}
function saveStatus(num,st){{
  const s=SEEDS.find(x=>x.num===num); if(!s) return;
  let arr=[]; try{{arr=JSON.parse(localStorage.getItem(AK)||"[]");}}catch{{}}
  const kw=s.name.replace(/\\n/g,"");
  const idx=arr.findIndex(e=>e.keyword===kw);
  const entry={{keyword:kw,category:AK,stage:st==="done"?"forest":"seed",updatedAt:new Date().toISOString()}};
  if(idx>=0) arr[idx]={{...arr[idx],...entry}}; else arr.unshift(entry);
  localStorage.setItem(AK,JSON.stringify(arr));
}}
loadStatus();

// ── Tree Layout ──
const NW=112, NH=54, NR=11, H_GAP=28, V_GAP=100, PAD=60;

function buildLayout(){{
  const childrenOf={{}};
  SEEDS.forEach(s=>{{childrenOf[s.num]=[];}});
  SEEDS.forEach(s=>{{if(s.parent!=null) childrenOf[s.parent].push(s.num);}});
  const roots=SEEDS.filter(s=>s.parent==null).map(s=>s.num);

  // Calculate subtree leaf count (for width)
  const leafW={{}};
  function calcW(n){{
    const ch=childrenOf[n];
    if(!ch.length){{ leafW[n]=NW+H_GAP; return leafW[n]; }}
    leafW[n]=ch.reduce((s,c)=>s+calcW(c),0);
    return leafW[n];
  }}
  roots.forEach(r=>calcW(r));

  // Assign X (center parent over children)
  const px={{}};
  function assignX(n,left){{
    const ch=childrenOf[n];
    if(!ch.length){{ px[n]=left; return left+NW+H_GAP; }}
    let cl=left;
    ch.forEach(c=>{{ cl=assignX(c,cl); }});
    const fc=ch[0],lc=ch[ch.length-1];
    px[n]=(px[fc]+px[lc]+NW)/2-NW/2;
    return cl;
  }}
  let rl=PAD;
  roots.forEach(r=>{{ rl=assignX(r,rl); }});

  // Y positions by level
  const levelY={{}};
  LEVELS.forEach((lv,i)=>{{ levelY[lv]=PAD+i*(NH+V_GAP); }});

  SEEDS.forEach(s=>{{
    s._x=px[s.num]; s._y=levelY[s.level];
    s._cx=s._x+NW/2; s._cy=s._y+NH/2;
  }});
  const svgW=Math.max(rl+PAD, 900);
  const svgH=PAD+4*(NH+V_GAP)+NH+PAD;
  return {{svgW,svgH,childrenOf,roots,levelY}};
}}

const SVG="http://www.w3.org/2000/svg";
function el(tag,a={{}},t){{
  const e=document.createElementNS(SVG,tag);
  Object.entries(a).forEach(([k,v])=>e.setAttribute(k,v));
  if(t!=null)e.textContent=t;
  return e;
}}

let selNum=null;

function build(){{
  const {{svgW,svgH,childrenOf,roots,levelY}}=buildLayout();
  const svg=document.getElementById("svg");
  svg.innerHTML="";
  svg.setAttribute("width",svgW);
  svg.setAttribute("height",svgH);
  svg.setAttribute("viewBox",`0 0 ${{svgW}} ${{svgH}}`);

  const defs=el("defs");
  // Gradients per level
  LEVELS.forEach(lv=>{{
    const lc=LC[lv];
    ["","_done"].forEach(suf=>{{
      const o1=suf?"0.32":"0.18", o2=suf?"0.14":"0.07";
      const g=el("linearGradient",{{id:`g_${{lv}}${{suf}}`,x1:"0",y1:"0",x2:"0",y2:"1"}});
      g.appendChild(el("stop",{{offset:"0%","stop-color":lc.c,"stop-opacity":o1}}));
      g.appendChild(el("stop",{{offset:"100%","stop-color":lc.c,"stop-opacity":o2}}));
      defs.appendChild(g);
    }});
  }});
  // Arrowhead
  const mk=el("marker",{{id:"arr",markerWidth:"7",markerHeight:"7",refX:"6",refY:"3.5",orient:"auto"}});
  mk.appendChild(el("polygon",{{points:"0 0,7 3.5,0 7",fill:"rgba(201,168,76,.3)"}}));
  defs.appendChild(mk);
  svg.appendChild(defs);

  // Level bands & labels
  LEVELS.forEach((lv,li)=>{{
    const lc=LC[lv]; const y=levelY[lv];
    // Band
    svg.appendChild(el("rect",{{x:0,y:y-12,width:svgW,height:NH+24,fill:li%2?"rgba(255,255,255,.007)":"transparent"}}));
    // Dashed separator
    if(li>0) svg.appendChild(el("line",{{x1:0,y1:y-16,x2:svgW,y2:y-16,stroke:lc.r+".1)","stroke-width":"1","stroke-dasharray":"6 10"}}));
    // Left label chip
    const lg=el("g");
    lg.appendChild(el("rect",{{x:8,y:y+NH/2-9,width:72,height:18,rx:9,fill:lc.r+".1)",stroke:lc.r+".28)","stroke-width":"1"}}));
    lg.appendChild(el("text",{{x:44,y:y+NH/2,"dominant-baseline":"central","text-anchor":"middle",
      fill:lc.c,"font-size":"9","font-family":"Noto Sans JP","font-weight":"900","letter-spacing":"1"}},
      `${{LI[lv]}} ${{lv}}`));
    // Right label
    lg.appendChild(el("text",{{x:svgW-12,y:y+NH/2,"dominant-baseline":"central","text-anchor":"end",
      fill:lc.r+".4)","font-size":"9","font-family":"Noto Sans JP","font-weight":"700"}},
      LDESCS[lv]));
    svg.appendChild(lg);
  }});

  // ── EDGES (drawn below nodes) ──
  SEEDS.forEach(s=>{{
    if(s.parent==null) return;
    const p=SEEDS.find(x=>x.num===s.parent); if(!p) return;
    const lc=LC[s.level];
    const x1=p._cx, y1=p._y+NH;
    const x2=s._cx, y2=s._y;
    const my=(y1+y2)/2;
    // Curved bezier branch
    svg.appendChild(el("path",{{
      d:`M${{x1}},${{y1}} C${{x1}},${{my}},${{x2}},${{my}},${{x2}},${{y2}}`,
      fill:"none",stroke:lc.r+".22)","stroke-width":"1.8",
      "stroke-linecap":"round"
    }}));
  }});

  // ROOT horizontal flow arrows
  const rootSeeds=SEEDS.filter(s=>s.parent==null);
  for(let i=0;i<rootSeeds.length-1;i++){{
    const a=rootSeeds[i],b=rootSeeds[i+1];
    svg.appendChild(el("path",{{
      d:`M${{a._x+NW+4}},${{a._cy}} L${{b._x-4}},${{b._cy}}`,
      fill:"none",stroke:"rgba(201,168,76,.2)","stroke-width":"1.2","marker-end":"url(#arr)"
    }}));
  }}

  // ── NODES ──
  let nDone=0,nWip=0;
  SEEDS.forEach(s=>{{
    const st=statusMap[s.num]||"none";
    if(st==="done")nDone++; else if(st==="wip")nWip++;
    const lc=LC[s.level];
    const isSel=selNum===s.num;
    const g=el("g",{{}});

    // Glow (selected or done)
    if(isSel||st==="done"){{
      svg.appendChild(el("rect",{{
        x:s._x-4,y:s._y-4,width:NW+8,height:NH+8,rx:NR+3,ry:NR+3,
        fill:"none",stroke:lc.c,"stroke-width":isSel?"2":"1","opacity":"0.45"
      }}));
    }}

    // Main rect
    const fill=`url(#g_${{s.level}}${{st==="done"?"_done":""}})`;
    const strk=st==="done"?lc.r+"0.7)":st==="wip"?"rgba(87,200,124,.55)":lc.r+"0.32)";
    g.appendChild(el("rect",{{x:s._x,y:s._y,width:NW,height:NH,rx:NR,ry:NR,fill,stroke:strk,"stroke-width":isSel?"2.5":"1.5"}}));

    // Left accent bar
    g.appendChild(el("rect",{{x:s._x,y:s._y+7,width:4,height:NH-14,rx:2,fill:lc.r+"0.75)"}}));

    // Seed number
    g.appendChild(el("text",{{x:s._x+10,y:s._y+12,fill:lc.r+"0.65)","font-size":"8","font-family":"Noto Sans JP","font-weight":"700"}},
      String(s.num).padStart(2,"0")));

    // Seed name
    const parts=s.name.split("\\n");
    parts.forEach((part,pi)=>{{
      const ny=parts.length===1?s._cy:s._cy+(pi-0.5)*13;
      g.appendChild(el("text",{{
        x:s._x+NW/2,y:ny,
        "dominant-baseline":"central","text-anchor":"middle",
        fill:st==="done"?lc.c:"#f0eedd","font-size":"12","font-family":"Noto Serif JP","font-weight":"700"
      }},part));
    }});

    // Status
    if(st==="done") g.appendChild(el("text",{{x:s._x+NW-6,y:s._y+NH-7,"text-anchor":"end",fill:lc.r+"0.85)","font-size":"8","font-family":"Noto Sans JP","font-weight":"900"}},"✓"));
    else if(st==="wip") g.appendChild(el("text",{{x:s._x+NW-6,y:s._y+NH-7,"text-anchor":"end",fill:"rgba(87,200,124,.8)","font-size":"8","font-family":"Noto Sans JP","font-weight":"900"}},"●"));

    g.style.cursor="pointer";
    g.addEventListener("click",()=>openPanel(s.num));
    svg.appendChild(g);
  }});

  // Stats
  const f=id=>document.getElementById(id);
  f("cDone").textContent=`完了 ${{nDone}}`;
  f("cWip").textContent=`学習中 ${{nWip}}`;
  f("cNone").textContent=`未着手 ${{26-nDone-nWip}}`;
  f("pbFill").style.width=Math.round(nDone/26*100)+"%";
  f("pbLbl").textContent=`${{nDone}} / 26`;

  setTimeout(()=>{{
    const t=document.getElementById("tree");
    t.scrollLeft=(svgW-t.clientWidth)/2;
    t.scrollTop=0;
  }},60);
}}

// ── Panel ──
function openPanel(num){{
  selNum=num;
  const s=SEEDS.find(x=>x.num===num); if(!s) return;
  const lc=LC[s.level];
  const db=window[DBVAR]&&window[DBVAR][PFX+String(num).padStart(3,"0")];
  const st=statusMap[num]||"none";
  document.getElementById("pLevel").textContent=LI[s.level]+" "+s.level+" — "+LDESCS[s.level];
  document.getElementById("pLevel").style.cssText=`border-color:${{lc.c}};color:${{lc.c}};background:${{lc.r}}.09);`;
  document.getElementById("pTitle").textContent=s.name.replace(/\\n/g," ");
  const body=document.getElementById("pBody");
  body.innerHTML="";
  // Tagline
  const tl=document.createElement("div"); tl.className="tagline";
  tl.style.borderLeftColor=lc.c;
  tl.textContent=db?.tagline||s.sub; body.appendChild(tl);
  // Root questions
  if(db?.rootQuestions?.length){{
    const sec=document.createElement("div"); sec.className="sec";
    const lbl=document.createElement("div"); lbl.className="sec-lbl"; lbl.textContent="ROOT QUESTION"; sec.appendChild(lbl);
    db.rootQuestions.slice(0,3).forEach(q=>{{const d=document.createElement("div");d.className="rq";d.textContent="❓ "+q;sec.appendChild(d);}});
    body.appendChild(sec);
  }}
  // Stop points
  if(db?.stopPoints?.length){{
    const sec=document.createElement("div"); sec.className="sec";
    const lbl=document.createElement("div"); lbl.className="sec-lbl"; lbl.textContent="⏸ ストップポイント"; sec.appendChild(lbl);
    db.stopPoints.slice(0,5).forEach(p=>{{
      const btn=document.createElement("button"); btn.className="sp"; btn.textContent=p;
      btn.onclick=()=>window.open(STREAM+"?seed="+num,"_blank");
      sec.appendChild(btn);
    }});
    body.appendChild(sec);
  }}
  // Keywords
  if(db?.glossTerms?.length){{
    const sec=document.createElement("div"); sec.className="sec";
    const lbl=document.createElement("div"); lbl.className="sec-lbl"; lbl.textContent="📖 キーワード"; sec.appendChild(lbl);
    const row=document.createElement("div"); row.className="kws";
    db.glossTerms.slice(0,7).forEach(t=>{{const k=document.createElement("span");k.className="kw";k.textContent=typeof t==="string"?t:t.word;row.appendChild(k);}});
    sec.appendChild(row); body.appendChild(sec);
  }}
  // Actions
  const acts=document.createElement("div"); acts.className="acts";
  const bd=document.createElement("button"); bd.className="act"+(st==="done"?" done":"");
  bd.textContent=st==="done"?"✓ 完了済み":"✓ 完了にする";
  bd.onclick=()=>{{statusMap[num]=statusMap[num]==="done"?"none":"done";saveStatus(num,statusMap[num]);showToast(statusMap[num]==="done"?`「${{s.name.replace(/\\n/g," ")}}」を完了にしました`:"完了を取り消しました");build();openPanel(num);}};
  const bw=document.createElement("button"); bw.className="act"+(st==="wip"?" wip":"");
  bw.textContent=st==="wip"?"● 学習中":"● 学習中にする";
  bw.onclick=()=>{{statusMap[num]=statusMap[num]==="wip"?"none":"wip";saveStatus(num,statusMap[num]);build();openPanel(num);}};
  acts.appendChild(bd); acts.appendChild(bw); body.appendChild(acts);
  const lnk=document.createElement("a"); lnk.className="p-link";
  lnk.href=STREAM+"?seed="+num; lnk.target="_blank";
  lnk.textContent="📡 この Seed で配信ページを開く ↗"; body.appendChild(lnk);
  document.getElementById("panel").classList.add("open");
  build();
}}

function closePanel(){{
  selNum=null;
  document.getElementById("panel").classList.remove("open");
  build();
}}

// ── Drag ──
(()=>{{
  const t=document.getElementById("tree");
  let dr=false,sx,sy,sl,st2;
  t.addEventListener("mousedown",e=>{{if(e.target.closest(".legend"))return;dr=true;sx=e.pageX-t.offsetLeft;sy=e.pageY-t.offsetTop;sl=t.scrollLeft;st2=t.scrollTop;}});
  t.addEventListener("mousemove",e=>{{if(!dr)return;e.preventDefault();t.scrollLeft=sl-(e.pageX-t.offsetLeft-sx);t.scrollTop=st2-(e.pageY-t.offsetTop-sy);}});
  t.addEventListener("mouseup",()=>dr=false);
  t.addEventListener("mouseleave",()=>dr=false);
}})();

// ── Toast ──
let tt;
function showToast(m){{const t=document.getElementById("toast");t.textContent=m;t.classList.add("on");clearTimeout(tt);tt=setTimeout(()=>t.classList.remove("on"),2400);}}

build();
}})();
</script>
</body>
</html>'''

import os
out = os.path.dirname(os.path.abspath(__file__))
for slug,subj in SUBJECTS.items():
    p = os.path.join(out,f"{slug}.html")
    open(p,"w",encoding="utf-8").write(make_html(slug,subj))
    print(f"{slug}.html written")
print("Done.")
