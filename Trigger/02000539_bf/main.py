""" trigger/02000539_bf/main.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_ladder(trigger_ids=[601])
        self.set_ladder(trigger_ids=[602])
        self.set_ladder(trigger_ids=[603])
        self.set_ladder(trigger_ids=[604])
        self.set_ladder(trigger_ids=[605])
        self.set_ladder(trigger_ids=[606])
        self.set_onetime_effect(id=101, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=102, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=103, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=104, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=105, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=106, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_mesh(trigger_ids=[904,905,906,907,908,909], visible=True)
        self.set_mesh(trigger_ids=[910,911,912,913,921,914,915,922,916,917,918,919,920,923,924,925,926,927])
        self.set_mesh(trigger_ids=[928,929,930,931,932,933,934,935,936,937])
        self.enable_spawn_point_pc(spawn_id=0, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=1)
        self.enable_spawn_point_pc(spawn_id=2)
        self.set_skill(trigger_ids=[2000])
        self.set_effect(trigger_ids=[3000])
        self.set_effect(trigger_ids=[3001])
        self.set_effect(trigger_ids=[3002])
        self.set_effect(trigger_ids=[3003])
        self.set_effect(trigger_ids=[3004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701], job_code=0):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102]):
            return 잠시쉬기(self.ctx)


class 잠시쉬기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[709], job_code=0):
            return 사다리생성하기(self.ctx)


class 사다리생성하기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[601], visible=True, enable=True)
        self.set_ladder(trigger_ids=[602], visible=True, enable=True)
        self.set_ladder(trigger_ids=[603], visible=True, enable=True)
        self.spawn_monster(spawn_ids=[203], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[706], job_code=0):
            return 잠시쉬기2(self.ctx)


class 잠시쉬기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000539_BF__MAIN__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 잠시쉬기3(self.ctx)


class 잠시쉬기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[904,905,906,907,908,909])
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[710], job_code=0):
            return 몬스터생성(self.ctx)


class 몬스터생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[203])
        self.spawn_monster(spawn_ids=[103,1031,1032,1033,1034])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[103,1031,1032,1033,1034]):
            return 다음몬스터생성조건체크(self.ctx)


class 다음몬스터생성조건체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000539_BF__MAIN__1$')
        self.spawn_monster(spawn_ids=[107,1071,1072])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 다음몬스터생성(self.ctx)


class 다음몬스터생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[105,1051,1052], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[107,1071,1072,105,1051,1052]):
            return NPC생성1(self.ctx)


class NPC생성1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000539_BF__MAIN__2$')
        self.set_effect(trigger_ids=[3000], visible=True)
        self.spawn_monster(spawn_ids=[201], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[707], job_code=0):
            return NPC생성2(self.ctx)


class NPC생성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000539_BF__MAIN__3$')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_500')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 다리만들기1(self.ctx)


class 다리만들기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_mesh(trigger_ids=[910,911], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 다리만들기2(self.ctx)


class 다리만들기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000539_BF__MAIN__4$')
        self.set_mesh(trigger_ids=[912,913,921], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 다리만들기3(self.ctx)


class 다리만들기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[914,915,922], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 다리만들기4(self.ctx)


class 다리만들기4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[916,917,918], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 다리만들기5(self.ctx)


class 다리만들기5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[919,920,926,922,927], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 다리만들기6(self.ctx)


class 다리만들기6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[923,924,925], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[708], job_code=0):
            return 다음몬스터생성1(self.ctx)


class 다음몬스터생성1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202], auto_target=False)
        self.spawn_monster(spawn_ids=[111,1111,1112,112,1121])
        self.side_npc_talk(npc_id=11004644, illust='SlaveMan3_normal', duration=3000, script='$02000539_BF__MAIN__5$')
        self.enable_spawn_point_pc(spawn_id=0)
        self.enable_spawn_point_pc(spawn_id=1, is_enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[111,1111,1112,112,1121]):
            return 다음몬스터생성조건체크2(self.ctx)


class 다음몬스터생성조건체크2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000539_BF__MAIN__6$')
        self.spawn_monster(spawn_ids=[113,1131,1132,1133,1134])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[705], job_code=0):
            return 다음몬스터생성조건체크3(self.ctx)


class 다음몬스터생성조건체크3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[3001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[113,1131,1132,1133,1134]):
            return 두번째다리만들기1(self.ctx)


class 두번째다리만들기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[204], auto_target=False)
        self.side_npc_talk(npc_id=11004644, illust='SlaveMan3_normal', duration=3000, script='$02000539_BF__MAIN__7$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[704], job_code=0):
            return 두번째다리만들기2(self.ctx)


class 두번째다리만들기2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째사다리생성하기1(self.ctx)


class 두번째사다리생성하기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000539_BF__MAIN__8$')
        self.set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_mesh(trigger_ids=[928,929,930,931,932,933,934,935,936,937], visible=True)
        self.set_ladder(trigger_ids=[604], visible=True, enable=True)
        self.set_ladder(trigger_ids=[605], visible=True, enable=True)
        self.set_ladder(trigger_ids=[606], visible=True, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 다음몬스터생성3(self.ctx)


class 다음몬스터생성3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[104,1041], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[104,1041]):
            return 보스문으로이동(self.ctx)


class 보스문으로이동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[711], job_code=0):
            return 벽부시기3단계(self.ctx)


class 벽부시기3단계(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=105, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_mesh(trigger_ids=[938,939,940,941,942,943])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[702], job_code=0):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004644, illust='SlaveMan3_normal', duration=3000, script='$02000539_BF__MAIN__9$')
        self.enable_spawn_point_pc(spawn_id=1)
        self.enable_spawn_point_pc(spawn_id=2, is_enable=True)
        self.spawn_monster(spawn_ids=[119])
        self.set_onetime_effect(id=106, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 보스등장3(self.ctx)


class 보스등장3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[3002], visible=True)
        self.set_effect(trigger_ids=[3003], visible=True)
        self.set_effect(trigger_ids=[3004], visible=True)
        self.set_skill(trigger_ids=[2000], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[119]):
            return 잠시쉬기4(self.ctx)


class 잠시쉬기4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000539_BF__MAIN__10$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 포탈활성화(self.ctx)


class 포탈활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = idle
