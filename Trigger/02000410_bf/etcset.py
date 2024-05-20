""" trigger/02000410_bf/etcset.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=750) >= 1:
            # MS2TriggerBox   TriggerObjectID = 750, 이 트리거 박스 안에 플레이어가 한명이라도 체크 되면, 750은 스타팅 지점 전투판 다  포함되는 범위, 700은 전투판만 포함되는 범위
            return 타이머(self.ctx)


class 타이머(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=28000):
            self.set_event_ui(type=1, arg2='$02000410_BF__BARRICADE_GIVEUP_0$', arg3='5000')
            self.dungeon_enable_give_up(is_enable=True)
            return 입구포탈제거(self.ctx)


class 입구포탈제거(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            # 스타팅지점에서 메인 전투판으로 보내주는 포탈을 30초 지나면 제거시켜서 다시 진입하지 못하게 막음,   arg1="3" 은 포탈ID
            self.set_portal(portal_id=3)
            return 보스HP체크(self.ctx)


class 보스HP체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        """
        condition name="CheckNpcDamage"   파라미터 기능 설명
        
                    spawnPointID: 체크할 NPC스폰포인트ID 스포너 안에 여러 NPC가 있을 경우 맨 첫 NPC를 체크합니다. 
                    damageRate: 누적 대미지 기준 값 1.0 일경우 해당 npc의 maxHP 0.5의 경우 50% 
                    operator: 연산자 기준 입니다 생략시 해당 값 이상 (GreaterEqual 이며) 다음 옵션을 사용 가능합니다. 
                    Greater,
                    GreaterEqual,
                    Equal,
                    LessEqual,
                    Less,
        """
        if self.npc_damage(spawn_id=102) >= 1.0:
            # 인페르녹 보스 스폰하기, 스폰ID : 102
            # 이때 보스 HP에 있는 인페르녹의 보호막 이펙트와 쉴드 버프 아이콘을 제거시겨서 보스 100% 클이어 조건이 되었음을 알림
            # 여기서 전투판 안에 있는 몬스터인 인페르녹에게 50004522 버프를 부여하여  인페르녹의 보호막 이펙트와 쉴드 버프 아이콘 출력 용도인 50004521 애디셔널을 제거시킴
            self.add_buff(box_ids=[102], skill_id=50004522, level=1)
            # 몬스터에게 애디셔널 거는 경우:  arg4 = "타겟이 몬스터로 하려면 1 인 경우  ->    arg1 = "몬스터스폰ID", arg2 = "애디셔널코드", arg3 = "애디셔널레벨", arg4 = "타겟이 몬스터로 하려면 1설정"
            # 플레이어에게 애디셔널 거는 경우:  arg4 = "타겟이 플레이어로 하려면 0   인 경우  ->  arg1 = "트리거박스ID", arg2 = "애디셔널코드", arg3 = "애디셔널레벨", arg4 = "타겟이 플레이어로 하려면 0 설정"
            # 레드마인 버그 #46130 이슈로 인페르녹 보스는 대포 석궁 펫 등 으로 플레이어 스킬 이외에 추가 대미지를 받는 요소가  많이 있기 때문에, 트리거에서 인페르녹 HP 100% 다 깎았는지를 체크하여 트리거 신호 보내는 방식으로 해야 함
            # ## 한국용 인페르녹 기준 HP 다 깎아서 보호막이 사라지면 인페르녹 HP 100% 깎는 던전미션 클리어 하도록 트리거에서 신호 보내기
            self.dungeon_mission_complete(feature='DungeonRankBalance_01', mission_id=24090004)
            # ## 중국용 인페르녹 기준 HP 다 깎아서 보호막이 사라지면 인페르녹 HP 100% 깎는 던전미션 클리어 하도록 트리거에서 신호 보내기
            self.dungeon_mission_complete(feature='DungeonRankBalance_02', mission_id=24090014)
            return 메시지알림(self.ctx)


class 메시지알림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 인페르녹의 쉴드가 사라졌다는 것을 메시지로 알려줌
        self.show_guide_summary(entity_id=20041005, text_id=20041005)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=20041005)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
