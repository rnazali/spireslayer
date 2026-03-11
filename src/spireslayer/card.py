class Card(object):
    def __init__(self, id: str, misc: int = 0, upgrades: int = 1) -> None:
        super().__init__()
        self.id = id
        self.misc = misc
        self.upgrades = upgrades

    def to_json(self):
        return {
            "id": self.id,
            "misc": self.misc,
            "upgrades": self.upgrades
        }

    class Ironclad:
        # Starter Cards
        BASH = "Bash"
        DEFEND_R = "Defend"
        STRIKE_R = "Strike"

        # Common Cards
        ANGER = "Anger"
        ARMAMENTS = "Armaments"
        BODY_SLAM = "Body Slam"
        CLASH = "Clash"
        CLEAVE = "Cleave"
        CLOTHESLINE = "Clothesline"
        FLEX = "Flex"
        HAVOC = "Havoc"
        HEADBUTT = "Headbutt"
        HEAVY_BLADE = "Heavy Blade"
        IRON_WAVE = "Iron Wave"
        PERFECTED_STRIKE = "Perfected Strike"
        POMMEL_STRIKE = "Pommel Strike"
        SHRUG_IT_OFF = "Shrug it Off"
        SWORD_BOOMERANG = "Sword Boomerang"
        THUNDERCLAP = "Thunderclap"
        TRUE_GRIT = "True Grit"
        TWIN_STRIKE = "Twin Strike"
        WARCRY = "Warcry"
        WILD_STRIKE = "Wild Strike"

        # Uncommon Cards
        BATTLE_TRANCE = "Battle Trance"
        BLOOD_FOR_BLOOD = "Blood for Blood"
        BLOODLETTING = "Bloodletting"
        BURNING_PACT = "Burning Pact"
        CARNAGE = "Carnage"
        COMBUST = "Combust"
        DARK_EMBRACE = "Dark Embrace"
        DISARM = "Disarm"
        DROPKICK = "Dropkick"
        DUAL_WIELD = "Dual Wield"
        ENTRENCH = "Entrench"
        EVOLVE = "Evolve"
        FEEL_NO_PAIN = "Feel No Pain"
        FIRE_BREATHING = "Fire Breathing"
        FLAME_BARRIER = "Flame Barrier"
        GHOSTLY_ARMOR = "Ghostly Armor"
        HEMOKINESIS = "Hemokinesis"
        INFERNAL_BLADE = "Infernal Blade"
        INFLAME = "Inflame"
        INTIMIDATE = "Intimidate"
        METALLICIZE = "Metallicize"
        POWER_THROUGH = "Power Through"
        PUMMEL = "Pummel"
        RAGE = "Rage"
        RAMPAGE = "Rampage"
        RECKLESS_CHARGE = "Reckless Charge"
        RUPTURE = "Rupture"
        SEARING_BLOW = "Searing Blow"
        SECOND_WIND = "Second Wind"
        SEEING_RED = "Seeing Red"
        SENTINEL = "Sentinel"
        SEVER_SOUL = "Sever Soul"
        SHOCKWAVE = "Shockwave"
        SPOT_WEAKNESS = "Spot Weakness"
        UPPERCUT = "Uppercut"
        WHIRLWIND = "Whirlwind"

        # Rare Cards
        BARRICADE = "Barricade"
        BERSERK = "Berserk"
        BLUDGEON = "Bludgeon"
        BRUTALITY = "Brutality"
        CORRUPTION = "Corruption"
        DEMON_FORM = "Demon Form"
        DOUBLE_TAP = "Double Tap"
        EXHUME = "Exhume"
        FEED = "Feed"
        FIEND_FIRE = "Fiend Fire"
        IMMOLATE = "Immolate"
        IMPERVIOUS = "Impervious"
        JUGGERNAUT = "Juggernaut"
        LIMIT_BREAK = "Limit Break"
        OFFERING = "Offering"
        REAPER = "Reaper"
