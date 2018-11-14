import random

tag_list = ['<time>', '<home_team_name>', '<home_team_score>', '<away_team_name>',
            '<away_star_score>', '<home_star_name>', '<home_star_score>', '<away_star_score>']


def choice_template(template_type: int) -> str:
    type_0_templates = [
        "<time>，<away_team_name>队手感火热，在<away_star_name>的带领下打出一波<away_team_score>分的进攻波，以<home_star_name>为核心的<home_team_name>队奋力直追，不过分差依然被拉大都<score_gap>分。",
        "<time>，<away_team_name>队的<away_star_name>表现神勇，连突带投，顶着<home_team_name>队同样疯狂的进攻火力，帮助<away_team_name>队拉大分差。",
        "<time>，<home_team_name>队的<home_star_name>与<away_team_name>队的<away_star_name>展开对轰，怎奈<away_star_name>技高一筹，<away_team_name>成功将分差拉大到<score_gap>分。"]

    type_1_templates = ["<time>，<away_team_name>队虽然手感不顺，但防守端在<away_star_name>的指挥下表现的十分顽强，依然将分差拉大到<score_gap>分。",
                         "<time>，<away_team_name>队在篮下建立起钢铁防线，<home_team_name>队的<home_star_name>等大将得分异常艰难， 似乎难以扭转颓势。",
                         "<time>，防守赢得总冠军似乎是一条永恒的真理，在<away_star_name>的带领下<away_team_name>的防守出色到连一只苍蝇都飞不过去，<home_team_name>显得有些无可奈何，分差被越拉越大。"]

    type_2_templates = [
        "<time>，<away_team_name>队的<away_star_name>似乎变得不可阻挡，他不仅在进攻端为球队贡献了<away_star_score>分，防守端也出色的完成了防守任务，<home_team_name>队仿佛梦游了一般，落后到<score_gap>分。",
        "<time>，在<away_star_name>的带领下，<away_team_name>在攻防两端均打出统治力，比分被越拉越大。"]

    type_3_templates = ["<time>，在<away_star_name>的带领下，<away_team_name>继续扩大着领先优势。",
                         "<time>，<away_team_name>多点开花，打出一波<away_team_score>分的进攻波，领先优势更加稳固了。"]

    type_4_templates = [
        "<time>，<away_team_name>队进攻端表现神勇，在<away_star_name>的带领下打出一波<away_team_score>分的进攻波，建立起了<score_gap>分的领先优势。",
        "<time>，<home_team_name>队的<home_star_name>表现神勇，接连砍分；怎奈<away_team_name>，在<away_star_name>的梳理下，进攻端更加高效，成功取得<score_gap>分的领先。",
        "<time>，<home_team_name>队的<home_star_name>与<away_team_name>队的<away_star_name>展开对轰，怎奈<away_star_name>技高一筹，领先到了<score_gap>分。"]

    type_5_templates = ["<time>，在外线接连打铁的情况下，凭借有效的防守，<away_team_name>还是建立起了<score_gap>分的领先。",
                         "<time>，强硬的防守让双方的得分都变得的艰难，不过随着一波<away_team_score>：<home_team_score>的进攻，<team_name>队还是保持着<score_gap>分的领先。"]

    type_6_templates = [
        "<time>，<away_team_name>队的<away_star_name>打破了场上的僵局，得到<away_star_score>分，帮<away_team_name>队领先到<score_gap>分。",
        "<time>，在<away_star_name>的带领下，<away_team_name>在攻防两端均打出统治力，比分有被拉大的趋势。"]

    type_7_templates = ["<time>，在<away_star_name>的带领下，<away_team_name>建立起了<score_gap>分的领先优势。",
                         "<time>，<away_team_name>与<home_team_name>相比，明显是更加投入的一方，他们稳扎稳打，建立了<score_gap>分的领先。"]

    type_8_templates = [
        "<time>，双方进攻端火力全开，<away_team_name>队更是手热如火，一波<away_team_score>：<home_team_score>的进攻波，缩小比分，让球队看到胜利的曙光。",
        "<time>，面对着巨大的落后和对方猛烈的进攻火力，<away_team_name>队的<away_star_name>奋起直追，得到<away_ster_score>分，将分差迫近至<score_gap>分。",
        "<time>，<home_team_name>队的<home_star_name>与<away_team_name>队的<away_star_name>展开对轰，怎奈<away_star_name>技高一筹，将落后缩小到<score_gap>分。"]

    type_9_templates = ["<time>，双方得分效率均有下降，但<away_team_name>队仍然靠着自己的拼搏，奋力直追，分差被大幅缩小。",
                         "<time>，<away_team_name>队奋力防守，<home_team_name>队也不甘示弱，连续的进攻转换，<home_team_name>的优势被渐渐蚕食。"]

    type_10_templates = [
        "<time>，在取得领先之后，<home_team_name>队明显在心态上有些松懈，被<away_team_name>抓住了机会，在<away_star_name>的带领下送上一波<away_team_score>比<home_team_score>的进攻波，缩小了分差。",
        "<time>，失败二字显然不存在于<away_team_name>队的基因中，在<away_star_name>的带领下，全队在攻防两端打出统治力，狠狠咬住比分。",
        "<time>，<away_team_name>手感回暖，其中<away_star_name>连续得分，打出一波<away_team_score>:<home_team_score>的进攻波，缩小落后。"]

    type_11_templates = ["<time>，<away_team_name>不甘示弱，在<away_star_name>的带领下不断追赶比分，缩小分差。",
                         "<time>，<away_team_name>表现得很顽强，把分差缩小到了<score_gap>分。"]

    type_12_templates = [
        "<time>，<home_team_name>的<home_star_name>和<away_team_name>的<away_star_name>协力为球迷奉上了一场对攻大战，然而分差依然十分胶着。",
        "<time>，<home_team_name>的<home_star_name>连砍<home_star_score>分，<away_team_name>的<away_star_name>也贡献了<away_star_score>分，但任谁也无法拉开差距。",
        "<time>，双方打得难解难分，运动战中连连得分，十分胶着，多次打平。"]

    type_13_templates = ["<time>，双方都疯狂打铁，场上的进攻似乎阻塞住了。",
                         "<time>,强而有力的防守力度，让双方的进攻效率都有所下降，但攻防之间，我们可以看到两只球队都实力不俗。"]

    type_14_templates = ["<time>，双方得分有来有往，比分焦灼。"]

    type_15_templates = ["<time>，双方得分有来有往，比分焦灼。"]

    type_16_templates = [
        "<time>，<home_team_name>队手感火热，在<home_star_name>的带领下打出一波<home_team_score>分的进攻波，以<away_star_name>为核心的<away_team_name>队奋力直追，不过分差依然被拉大都<score_gap>分。",
        "<time>，<home_team_name>队的<home_star_name>表现神勇，连突带投，顶着<away_team_name>队同样疯狂的进攻火力，帮助<home_team_name>队拉大分差。",
        "<time>，<away_team_name>队的<away_star_name>与<home_team_name>队的<home_star_name>展开对轰，怎奈<home_star_name>技高一筹，<home_team_name>成功将分差拉大到<score_gap>分。"]

    type_17_templates = ["<time>，<home_team_name>队虽然手感不顺，但防守端在<home_star_name>的指挥下表现的十分顽强，依然将分差拉大到<score_gap>分。",
                        "<time>，<home_team_name>队在篮下建立起钢铁防线，<away_team_name>队的<away_star_name>等大将得分异常艰难， 似乎难以扭转颓势。",
                        "<time>，防守赢得总冠军似乎是一条永恒的真理，在<home_star_name>的带领下<home_team_name>的防守出色到连一只苍蝇都飞不过去，<away_team_name>显得有些无可奈何，分差被越拉越大。"]

    type_18_templates = [
        "<time>，<home_team_name>队的<home_star_name>似乎变得不可阻挡，他不仅在进攻端为球队贡献了<home_star_score>分，防守端也出色的完成了防守任务，<away_team_name>队仿佛梦游了一般，落后到<score_gap>分。",
        "<time>，在<home_star_name>的带领下，<home_team_name>在攻防两端均打出统治力，比分被越拉越大。"]

    type_19_templates = ["<time>，在<home_star_name>的带领下，<home_team_name>继续扩大着领先优势。",
                        "<time>，<home_team_name>多点开花，打出一波<home_team_score>分的进攻波，领先优势更加稳固了。"]

    type_20_templates = [
        "<time>，<home_team_name>队进攻端表现神勇，在<home_star_name>的带领下打出一波<home_team_score>分的进攻波，建立起了<score_gap>分的领先优势。",
        "<time>，<away_team_name>队的<away_star_name>表现神勇，接连砍分；怎奈<home_team_name>，在<home_star_name>的梳理下，进攻端更加高效，成功取得<score_gap>分的领先。",
        "<time>，<away_team_name>队的<away_star_name>与<home_team_name>队的<home_star_name>展开对轰，怎奈<home_star_name>技高一筹，领先到了<score_gap>分。"]

    type_21_templates = ["<time>，在外线接连打铁的情况下，凭借有效的防守，<home_team_name>还是建立起了<score_gap>分的领先。",
                        "<time>，强硬的防守让双方的得分都变得的艰难，不过随着一波<home_team_score>：<away_team_score>的进攻，<team_name>队还是保持着<score_gap>分的领先。"]

    type_22_templates = [
        "<time>，<home_team_name>队的<home_star_name>打破了场上的僵局，得到<home_star_score>分，帮<home_team_name>队领先到<score_gap>分。",
        "<time>，在<home_star_name>的带领下，<home_team_name>在攻防两端均打出统治力，比分有被拉大的趋势。"]

    type_23_templates = ["<time>，在<home_star_name>的带领下，<home_team_name>建立起了<score_gap>分的领先优势。",
                        "<time>，<home_team_name>与<away_team_name>相比，明显是更加投入的一方，他们稳扎稳打，建立了<score_gap>分的领先。"]

    type_24_templates = [
        "<time>，双方进攻端火力全开，<home_team_name>队更是手热如火，一波<home_team_score>：<away_team_score>的进攻波，缩小比分，让球队看到胜利的曙光。",
        "<time>，面对着巨大的落后和对方猛烈的进攻火力，<home_team_name>队的<home_star_name>奋起直追，得到<home_ster_score>分，将分差迫近至<score_gap>分。",
        "<time>，<away_team_name>队的<away_star_name>与<home_team_name>队的<home_star_name>展开对轰，怎奈<home_star_name>技高一筹，将落后缩小到<score_gap>分。"]

    type_25_templates = ["<time>，双方得分效率均有下降，但<home_team_name>队仍然靠着自己的拼搏，奋力直追，分差被大幅缩小。",
                        "<time>，<home_team_name>队奋力防守，<away_team_name>队也不甘示弱，连续的进攻转换，<away_team_name>的优势被渐渐蚕食。"]

    type_26_templates = [
        "<time>，在取得领先之后，<away_team_name>队明显在心态上有些松懈，被<home_team_name>抓住了机会，在<home_star_name>的带领下送上一波<home_team_score>比<away_team_score>的进攻波，缩小了分差。",
        "<time>，失败二字显然不存在于<home_team_name>队的基因中，在<home_star_name>的带领下，全队在攻防两端打出统治力，狠狠咬住比分。",
        "<time>，<home_team_name>手感回暖，其中<home_star_name>连续得分，打出一波<home_team_score>:<away_team_score>的进攻波，缩小落后。"]

    type_27_templates = ["<time>，<home_team_name>不甘示弱，在<home_star_name>的带领下不断追赶比分，缩小分差。",
                         "<time>，<home_team_name>表现得很顽强，把分差缩小到了<score_gap>分。"]

    templates = [type_0_templates, type_1_templates, type_2_templates, type_3_templates, type_4_templates,
                 type_5_templates, type_6_templates, type_7_templates, type_8_templates, type_9_templates,
                 type_10_templates, type_11_templates, type_12_templates, type_13_templates, type_14_templates,
                 type_15_templates, type_16_templates, type_17_templates, type_18_templates, type_19_templates,
                 type_20_templates, type_21_templates, type_22_templates, type_23_templates, type_24_templates,
                 type_25_templates, type_26_templates, type_27_templates]

    return random.choice(templates[template_type])
