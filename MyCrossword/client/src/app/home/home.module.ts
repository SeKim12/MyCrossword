import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { LoginComponent } from "./components/login.component";
import { UserComponent } from "./components/user.component";
import { FormsModule } from "@angular/forms";

@NgModule({
  declarations: [LoginComponent, UserComponent],
  imports: [CommonModule, FormsModule],
})
export class HomeModule {}
