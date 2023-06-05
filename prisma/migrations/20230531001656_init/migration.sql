-- CreateTable
CREATE TABLE "student" (
    "ra" INTEGER NOT NULL,
    "full_name" TEXT NOT NULL,
    "updated_at" TIMESTAMP(3) NOT NULL,
    "create_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "student_pkey" PRIMARY KEY ("ra")
);

-- CreateTable
CREATE TABLE "subject" (
    "id" SERIAL NOT NULL,
    "name" TEXT NOT NULL,
    "day_of_week" INTEGER NOT NULL,
    "start_hour" INTEGER NOT NULL,
    "end_hour" INTEGER NOT NULL,

    CONSTRAINT "subject_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "attendance" (
    "id" SERIAL NOT NULL,
    "student_ra" INTEGER NOT NULL,
    "subject_id" INTEGER NOT NULL,
    "create_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "attendance_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "attendance" ADD CONSTRAINT "attendance_student_ra_fkey" FOREIGN KEY ("student_ra") REFERENCES "student"("ra") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "attendance" ADD CONSTRAINT "attendance_subject_id_fkey" FOREIGN KEY ("subject_id") REFERENCES "subject"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
