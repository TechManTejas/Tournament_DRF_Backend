from django.contrib import admin
from .models import Group, GroupTeam


class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "club", "tournament", "round")
    search_fields = ["name"]


admin.site.register(Group, GroupAdmin)


@admin.register(GroupTeam)
class GroupTeamAdmin(admin.ModelAdmin):
    list_display = ("team_record", "points", "goals_pos", "goals_neg")
