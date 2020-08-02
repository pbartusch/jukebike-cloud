import { Component, OnInit } from '@angular/core';
import { JukeBikeService, AdminSettings } from '../jukebike.service'

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})
export class AdminComponent implements OnInit {

  adminHint: string = ''
  settings: AdminSettings = new AdminSettings()

  constructor(
    private jukeBikeService: JukeBikeService
  ) { }

  ngOnInit(): void {
    this.jukeBikeService
      .getSettings()
      .then(s => {
        this.adminHint = 'Settings loaded!'
        this.settings = s
      })
  }

  submitAdminSettings() {
    this.jukeBikeService
      .setSettings(this.settings)
    this.adminHint = 'Settings saved!'
  }

}
