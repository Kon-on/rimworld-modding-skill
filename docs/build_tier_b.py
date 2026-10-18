# -*- coding: utf-8 -*-
"""Build Tier B: full field reference for ALL 254 def types found in RimWorld 1.7."""
import os, json, csv, collections

WS   = r"<REPO_ROOT>"
PROC = os.path.join(WS, "docs")
OUT  = os.path.join(WS, "library", "03-全量字段参考")

LINES = collections.OrderedDict([
    ("pawn",   "01-人物线"), ("item",  "02-物品线"), ("world", "03-世界线"),
    ("ideo",   "04-理念线"), ("visual","05-表现线"), ("system","06-系统线"),
])
LINE_NAME = {"pawn":"人物线","item":"物品线","world":"世界线",
             "ideo":"理念线","visual":"表现线","system":"系统线"}

LINE_OF = {}
def A(line, *names):
    for n in names:
        assert n not in LINE_OF, "dup " + n
        LINE_OF[n] = line

A("pawn", "AbilityCategoryDef","AbilityDef","AbilityGroupDef","BabyPlayDef","BackstoryDef",
 "BackStoryDef","BeardDef","BodyDef","BodyPartDef","BodyPartGroupDef","BodyPartTagDef",
 "BodyTypeDef","FleshTypeDef","FurDef","GeneCategoryDef","GeneDef","GeneTemplateDef","HairDef",
 "HeadTypeDef","HediffDef","HediffGiverSetDef","InspirationDef","InteractionDef","JoyGiverDef",
 "JoyKindDef","KnowledgeCategoryDef","LearningDesireDef","LifeStageDef","MechWeightClassDef",
 "MechWorkModeDef","MentalBreakDef","MentalFitDef","MentalStateDef","MutantDef","NeedDef",
 "PawnCapacityDef","PawnKindDef","PawnRelationDef","SkillDef","SurgeryOutcomeEffectDef",
 "TattooDef","ThoughtDef","TrainabilityDef","TrainableDef","TraitDef","XenotypeDef")

A("item", "ApparelLayerDef","ChemicalDef","DamageArmorCategoryDef","DamageDef",
 "InventoryStockGroupDef","RecipeDef","SpecialThingFilterDef","StuffAppearanceDef",
 "StuffCategoryDef","StyleCategoryDef","StyleItemCategoryDef","ThingCategoryDef","ThingDef",
 "ToolCapacityDef","WeaponCategoryDef","WeaponClassDef","WeaponClassPairDef","WeaponTraitDef")

A("world", "AnomalyPlaystyleDef","BiomeDef","BossDef","BossgroupDef","ClamorDef","ComplexLayoutDef",
 "ComplexThreatDef","CreepJoinerAggressiveDef","CreepJoinerBenefitDef","CreepJoinerDownsideDef",
 "CreepJoinerFormKindDef","CreepjoinerRejectionDef","DifficultyDef","EntityCategoryDef",
 "EntityCodexEntryDef","FactionDef","FeatureDef","GameConditionDef","GeneratedLocationDef",
 "GenStepDef","GoodwillSituationDef","GravshipComponentTypeDef","HibernatableStateDef",
 "HistoryEventDef","ImplementOwnerTypeDef","IncidentCategoryDef","IncidentDef","IncidentTargetTagDef",
 "InfectionPathwayDef","LandingOutcomeDef","LandmarkDef","LayoutDef","LayoutRoomDef","ManeuverDef",
 "MapGeneratorDef","MonolithLevelDef","NegativeFishingOutcomeDef","OrbitalDebrisDef",
 "PawnGroupKindDef","PawnsArrivalModeDef","PitGateIncidentDef",
 "PlanetLayerDef","PlanetLayerSettingsDef",
 "PsychicRitualDef_BloodRain","PsychicRitualDef_Brainwipe","PsychicRitualDef_Chronophagy",
 "PsychicRitualDef_ImbueDeathRefusal","PsychicRitualDef_NeurosisPulse","PsychicRitualDef_Philophagy",
 "PsychicRitualDef_PleasurePulse","PsychicRitualDef_Psychophagy","PsychicRitualDef_SkipAbduction",
 "PsychicRitualDef_SkipAbductionPlayer","PsychicRitualDef_SummonAnimals",
 "PsychicRitualDef_SummonFleshbeasts","PsychicRitualDef_SummonFleshbeastsPlayer",
 "PsychicRitualDef_SummonPitGate","PsychicRitualDef_SummonShamblers",
 "PsychicRitualDef_VoidProvocation","PsychicRitualRoleDef","PsychicRitualRoleDef_DeathRefusalTarget",
 "QuestScriptDef","RaidAgeRestrictionDef","RaidStrategyDef","RiverDef","RoadDef","RoadPathingDef",
 "RoadWorldLayerDef","RoofDef","RoomPart_BarricadeDef","RoomPart_CrateDef",
 "RoomPart_GestationTankDef","RoomPart_ThingDef","RoomPartDef","RoomRoleDef","RoomStatDef",
 "RoyalTitleDef","RoyalTitlePermitDef","ScatterableDef","ScenarioDef","ScenPartDef","ShipJobDef",
 "SitePartDef","SketchResolverDef","StorytellerDef","StructureLayoutDef",
 "StructureStructureLayoutDef","TaleDef","TerrainAffordanceDef","TerrainDef","TerrainTemplateDef",
 "ThingSetMakerDef","TileMutatorDef","TraderKindDef","TransportShipDef","WeatherDef",
 "WorldGenStepDef","WorldObjectDef")

A("ideo", "CultureDef","ExpectationDef","GatheringDef","GauranlenTreeModeDef","IdeoColorDef",
 "IdeoFoundationDef","IdeoIconDef","IdeoPresetCategoryDef","IdeoPresetDef","IdeoStoryPatternDef",
 "IssueDef","MeditationFocusDef","MemeDef","MemeGroupDef","PlaceDef","PreceptDef",
 "RitualAttachableOutcomeEffectDef","RitualBehaviorDef","RitualObligationTargetFilterDef",
 "RitualOutcomeEffectDef","RitualPatternDef","RitualTargetFilterDef","RitualVisualEffectDef")

A("visual", "AnimationDef","ColorDef","DrawStyleCategoryDef","DrawStyleDef","EffecterDef","FleckDef",
 "GlobalWorldDrawLayerDef","GraphicStateDef","ImpactSoundTypeDef","MaterialDef","MusicSequenceDef",
 "MusicTransitionDef","PawnColumnDef","PawnRenderNodeTagDef","PawnRenderTreeDef","PawnTableDef",
 "PrefabDef","RenderSkipFlagDef","ShaderDef","ShaderTypeDef","SongDef","SoundDef","SubcameraDef",
 "ThingStyleDef","TransferableSorterDef","XenotypeIconDef")

A("system", "BillRepeatModeDef","BillStoreModeDef","ConceptDef","DebugTabMenuDef",
 "DesignationCategoryDef","DesignationDef","DesignatorDropdownGroupDef","DrugPolicyDef","DutyDef",
 "ExpansionDef","GameSetupStepDef","HistoryAutoRecorderDef","HistoryAutoRecorderGroupDef",
 "InstructionDef","JobDef","jobDef","KeyBindingCategoryDef","KeyBindingDef","LetterDef",
 "LogEntryDef","MainButtonDef","MapMeshFlagDef","MessageTypeDef","OptionCategoryDef",
 "OrderedTakeGroupDef","PathGridDef","PrisonerInteractionModeDef","RecordDef","ResearchProjectDef",
 "ResearchProjectTagDef","ResearchTabDef","ReservationLayerDef","RuleDef","RulePackDef",
 "SlaveInteractionModeDef","StatCategoryDef","StatDef","ThinkTreeDef","TimeAssignmentDef",
 "TipSetDef","WorkGiverDef","WorkGiverEquivalenceGroupDef","WorkTypeDef")

KIND_CN = {"number":"数值","bool":"布尔","text":"文本","empty":"容器"}
def kind_cn(kinds):
    if not kinds: return "容器"
    return "/".join(KIND_CN.get(k, k) for k in kinds)

def esc(s):
    return str(s).replace("|", "\\|")

def bt(s):
    B = chr(96)
    return B + str(s) + B

def main():
    schema = json.load(open(os.path.join(PROC, "def-schema.json"), encoding="utf-8"))
    ex     = json.load(open(os.path.join(PROC, "def-examples.json"), encoding="utf-8"))
    types  = schema["defTypes"]
    B      = chr(96)

    # Windows 文件名不区分大小写，需处理大小写冲突的类型对
    groups = collections.defaultdict(list)
    for t in types:
        groups[t.lower()].append(t)
    FNAME, COLLISIONS = {}, {}
    for low, members in groups.items():
        members.sort(key=lambda n: -types[n]["instances"])
        for i, n in enumerate(members):
            FNAME[n] = n if i == 0 else n + "_variant" + (str(i) if i > 1 else "")
        if len(members) > 1:
            COLLISIONS[low] = members

    missing = sorted(set(types) - set(LINE_OF))
    extra   = sorted(set(LINE_OF) - set(types))
    if missing: print("UNCLASSIFIED:", missing)
    if extra:   print("NOT IN SCHEMA:", extra)
    assert not missing, "unclassified def types remain"

    os.makedirs(OUT, exist_ok=True)
    fdir = os.path.join(OUT, "字段")
    os.makedirs(fdir, exist_ok=True)

    total_rows = 0
    index_rows = []
    per_line = collections.OrderedDict((k, []) for k in LINES)

    for t, info in types.items():
        line   = LINE_OF[t]
        inst   = info["instances"]
        paths  = info["paths"]
        exinfo = ex.get(t, {})
        smallest = exinfo.get("smallest", {})
        median   = exinfo.get("median", {})
        allnames = exinfo.get("allDefNames", info.get("defNames", []))

        locs = []
        for cand in (smallest, median):
            f = cand.get("file")
            if f and f not in locs:
                locs.append(f)
        assert locs, "no location for " + t

        core = sorted([p for p, v in paths.items() if v["ratio"] >= 0.9], key=lambda s: s.lower())
        ordered = sorted(paths.keys(), key=lambda s: s.lower())

        L = []
        L.append("# " + t)
        L.append("")
        L.append("- **所属线**：" + LINE_NAME[line])
        L.append("- **原版实例数**：%d" % inst)
        L.append("- **字段路径数**：%d" % info["pathCount"])
        L.append("- **资料片**：" + ("、".join(info["expansions"]) or "—"))
        if info.get("classes"):
            L.append("- **Class 属性取值**：" + "、".join(bt(c) for c in sorted(info["classes"])[:6]))
        L.append("- **原版出处**：" + "、".join(bt(l) for l in locs[:4]))
        L.append("- **数据来源**：" + bt("docs/def-schema.json") + " + " + bt("docs/def-examples.json")
                 + "（由本机 RimWorld 1.7.4981 rev136 实测提取）")
        L.append("")
        L.append("## 一、最小真实范例（原版原样，可直接复制改名）")
        L.append("")
        if smallest.get("xml"):
            L.append(B*3 + "xml")
            L.append(smallest["xml"].strip("\n"))
            L.append(B*3)
            L.append("")
            L.append("> 来自 " + bt(smallest.get("file")) + "，defName = " + bt(smallest.get("defName"))
                     + "，XML 节点数 " + str(smallest.get("nodes")) + "（该类型中最小）")
        L.append("")
        L.append("## 二、核心字段（出现率 ≥90%，可视为必填）")
        L.append("")
        if core:
            L.append(B*3 + "text")
            for p in core:
                v = paths[p]
                sm = ("  例：" + " / ".join(v["samples"][:3])) if v["samples"] else ""
                L.append("%-46s [%s]%s" % (p, kind_cn(v["kind"]), sm))
            L.append(B*3)
        else:
            L.append("_该类型没有出现率≥90% 的字段（字段高度自由）。_")
        L.append("")
        L.append("## 三、全量字段表（%d 条路径）" % info["pathCount"])
        L.append("")
        L.append("| 路径 | 出现率 | 值类型 | 原版样例值 |")
        L.append("|---|---|---|---|")
        for p in ordered:
            v = paths[p]
            sm = " / ".join(v["samples"][:3]) if v["samples"] else ""
            L.append("| " + bt(esc(p)) + " | %.1f%% (%d/%d) | %s | %s |"
                     % (v["ratio"]*100, v["n"], inst, kind_cn(v["kind"]), esc(sm)[:110]))
            total_rows += 1
            per_line[line].append((t, p, v["n"], inst, round(v["ratio"], 4),
                                   kind_cn(v["kind"]), sm[:200], locs[0]))
        L.append("")
        L.append("## 四、原版 defName 一览（共 %d 个，列出前 60）" % len(allnames))
        L.append("")
        L.append(B*3 + "text")
        for i in range(0, min(len(allnames), 60), 4):
            L.append("  ".join("%-32s" % bt(n) for n in allnames[i:i+4]))
        L.append(B*3)
        if len(allnames) > 60:
            L.append("")
            L.append("_余下 %d 个 defName 见原版 " % (len(allnames)-60) + bt("Data/<资料片>/Defs") + " 对应目录。_")
        L.append("")

        with open(os.path.join(fdir, FNAME[t] + ".md"), "w", encoding="utf-8") as f:
            f.write("\n".join(L))

        index_rows.append({"line": line, "defType": t, "instances": inst,
                           "pathCount": info["pathCount"], "required": len(core),
                           "expansions": "、".join(info["expansions"]),
                           "sample": (allnames[0] if allnames else "")})

    with open(os.path.join(OUT, "字段总表.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["line","defType","path","present","instances","ratio","kind","samples","sourceFile"])
        for line in LINES:
            for row in per_line[line]:
                w.writerow([LINE_NAME[line]] + list(row))

    idx = []
    idx.append("# RimWorld 1.7 全量 Def 字段索引")
    idx.append("")
    idx.append("覆盖本机 RimWorld **1.7.4981 rev136** 的 " + bt("Data/<资料片>/Defs")
               + " 下实测出现的 **%d 种 Def 类型**、**%d 个 XML 文件**、**%d 个 Def 实例**、**%d 条字段路径**。"
               % (len(types), schema["defFilesParsed"], sum(i["instances"] for i in types.values()), total_rows))
    idx.append("")
    idx.append("每个类型一个文件：" + bt("字段/<DefType>.md") + "（含最小真实范例、核心字段、全量字段表、defName 一览）。")
    idx.append("机器可读版本：" + bt("字段总表.csv") + "。")
    idx.append("")
    idx.append("> 「出现率」= 该字段在该类型原版实例中的出现比例，可作「是否必填」的经验判据：≥90% 基本必填；40–90% 常见可选；<10% 属于特例用法。")
    idx.append("")
    if COLLISIONS:
        idx.append("## 大小写同名冲突")
        idx.append("")
        idx.append("原版 XML 里存在仅大小写不同的 Def 标签，Windows 无法用同一个文件名保存，故后者追加 `_variant`：")
        idx.append("")
        for low, members in sorted(COLLISIONS.items()):
            idx.append("- " + "、".join("%s（%d 实例）→ `%s.md`" % (m, types[m]["instances"], FNAME[m]) for m in members))
        idx.append("")
    idx.append("")
    for line in LINES:
        rows = [r for r in index_rows if r["line"] == line]
        rows.sort(key=lambda r: -r["pathCount"])
        idx.append("## %s（%d 种类型）" % (LINE_NAME[line], len(rows)))
        idx.append("")
        idx.append("| Def 类型 | 实例数 | 字段路径数 | 必填字段数 | 资料片 | 首样例 | 字段表 |")
        idx.append("|---|---|---|---|---|---|---|")
        for r in rows:
            idx.append("| %s | %d | %d | %d | %s | %s | [打开](字段/%s.md) |"
                       % (r["defType"], r["instances"], r["pathCount"], r["required"],
                          r["expansions"] or "—", bt(r["sample"]) if r["sample"] else "—", FNAME[r["defType"]]))
        idx.append("")
    with open(os.path.join(OUT, "00-字段索引.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(idx))

    print(json.dumps({"types": len(types), "fieldFiles": len(os.listdir(fdir)),
                      "totalFieldPaths": total_rows}, ensure_ascii=False))
    for k in LINES:
        print("  %-8s types=%3d paths=%6d" % (LINE_NAME[k], len(set(r[0] for r in per_line[k])), len(per_line[k])))

if __name__ == "__main__":
    main()
