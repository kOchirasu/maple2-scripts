""" trigger/80000022_bonus/prize.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154], visible=True)
        # 오브젝트 반응 이후 사라진 달토끼 대체인력 끈 상태로 정의
        self.set_actor(trigger_id=3000, initial_sequence='or_functobj_mortar_A01_off')
        self.set_interact_object(trigger_ids=[11000119], state=1) # 달토끼 오브젝트, 반응 가능으로 스폰
        self.set_portal(portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[301]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawn_ids=[201])
        self.create_item(spawn_ids=[202])
        self.create_item(spawn_ids=[203])
        self.create_item(spawn_ids=[204])
        self.create_item(spawn_ids=[205])
        self.create_item(spawn_ids=[206])
        self.create_item(spawn_ids=[207])
        self.create_item(spawn_ids=[208])
        self.create_item(spawn_ids=[209])
        self.create_item(spawn_ids=[210])
        self.create_item(spawn_ids=[211])
        self.create_item(spawn_ids=[212])
        self.create_item(spawn_ids=[213])
        self.create_item(spawn_ids=[216])
        self.create_item(spawn_ids=[217])
        self.create_item(spawn_ids=[218])
        self.create_item(spawn_ids=[219])
        self.create_item(spawn_ids=[220])
        self.create_item(spawn_ids=[221])
        self.create_item(spawn_ids=[222])
        self.create_item(spawn_ids=[226])
        self.create_item(spawn_ids=[227])
        self.create_item(spawn_ids=[228])
        self.create_item(spawn_ids=[229])
        self.create_item(spawn_ids=[230])
        self.create_item(spawn_ids=[231])
        self.create_item(spawn_ids=[232])
        self.create_item(spawn_ids=[233])
        self.create_item(spawn_ids=[234])
        self.create_item(spawn_ids=[235])
        self.create_item(spawn_ids=[243])
        self.create_item(spawn_ids=[244])
        self.create_item(spawn_ids=[245])
        self.create_item(spawn_ids=[246])
        self.create_item(spawn_ids=[247])
        self.create_item(spawn_ids=[248])
        self.create_item(spawn_ids=[250])
        self.create_item(spawn_ids=[251])
        self.create_item(spawn_ids=[255])
        self.create_item(spawn_ids=[256])
        self.create_item(spawn_ids=[257])
        self.create_item(spawn_ids=[258])
        self.create_item(spawn_ids=[259])
        self.create_item(spawn_ids=[260])
        self.create_item(spawn_ids=[261])
        self.create_item(spawn_ids=[262])
        self.create_item(spawn_ids=[263])
        self.create_item(spawn_ids=[264])
        self.create_item(spawn_ids=[265])
        self.create_item(spawn_ids=[266])
        self.create_item(spawn_ids=[267])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 오브젝트체크(self.ctx)


class 오브젝트체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[11000119], state=0):
            return 포탈생성(self.ctx)


class 포탈생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[11000119], state=2) # 달토끼 오브젝트, 사라짐
        # 오브젝트 반응 이후 사라진 달토끼 대체인력 켜기
        self.set_actor(trigger_id=3000, visible=True, initial_sequence='or_functobj_mortar_A01_off')
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    pass


initial_state = 입장
